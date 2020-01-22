# re is for regular expressions
import re
# sys is for command line arguments
import sys

#read in file
file_name = ""
if len(sys.argv) == 0:
    file_name = "in.txt"
else:
    file_name = sys.argv[1]
with open(file_name) as f:
    content = f.readlines()
f.close()


in_code = False  # used for multi-line code blocks
in_pre = False # used when existing file has a <pre> block
in_infobox = False  # used for infoboxs

for line in content:
    # remove problematic character combinations
    line = line.replace("# ", "#")

    # fix headers
    if line[0] == "=":
        line = line.replace("======", "###### ", 1)
        line = line.replace("======", "")
        line = line.replace("=====", "##### ", 1)
        line = line.replace("=====", "")
        line = line.replace("====", "#### ", 1)
        line = line.replace("====", "")
        line = line.replace("===", "### ", 1)
        line = line.replace("===", "")
        line = line.replace("==", "## ", 1)
        line = line.replace("==", "")
        line = line.replace("=", "# ", 1)
        line = line.replace("=", "")

    # fix URLs
    line = re.sub(r'(.*)\[(\S+)\.(\S*)\s(.+)\](.*)', r'\1[\4](\2.\3)\5', line)

    # fix code blocks
    line = line.replace("<code><pre>","<pre>")
    line = line.replace("</code></pre>","</pre>")
    if line.find("<pre>") != -1:
        in_pre = True
    if line.find("</pre>") != -1:
        in_pre = False
    if line[0] != " " and line[0] != "\n" and in_code and not in_pre:
        line = "</pre>\n" + line
        in_code = False
    if line[0] == " " and not in_code and not in_pre:
        line = line.replace(" ", "<pre> ", 1)
        in_code = True
    line.replace("</pre>#", "</pre>\n#")

    # fix infoboxes
    if line.find("{{Infobox") != -1:
        line = "## Information"
        in_infobox = True
    if in_infobox:
        line = line.replace("|", "*")
        if line.find("}}") != -1:
            line = "\n"
            in_infobox = False

    # fix lists
    line = line.replace("***", "        *")
    line = line.replace("**", "    *")
    line = line.replace("*", "* ")
    line = line.replace("  ", " ")

    # fix bold
    line = line.replace("'''", "**")

    # remove extra whitespace that the 'print' command adds
    line = line.replace("\n", "", 1)

    print(line)
