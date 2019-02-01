# Wiki
The repository tracking the tech director wiki

## Info about deployment
This repository is a 1:1 mirror of the internal git repository Github maintains for their wiki system. Particularly, this repo
mirrors https://github.com/CIF-Rochester/wiki/wiki.

What does this mean for you?

People can contribute to the wiki as if it was a normal Github project. The magic stuff is handled by these two scripts:

* sync.sh - This bash script will sync the changes between the real wiki and the mirrored one. If changes are made anywhere in the wiki,
someone with push access to this repo MUST run this script.
* push.sh - This bash script expects one argument in quotes. This will be the change message regarding what you've done. This is
used if you have cloned the repository on your computer and edited it locally and wish for the changes to be deployed. So running
`./push.sh "My short change description"` will commit your change to this repository and sync the changes.

## Implementation notes
You will likely be prompted for your Github credentials *twice* whenever you run a script which syncs the wiki repos. So pay attention
to the scripts output! And if you don't already know, if you use 2FA in Github the password you put in will not be your password, but 
rather a "Personal Access Token" which must be generated with the `repo` permission here: https://github.com/settings/tokens (or, alternatively, use [SSH Keys](https://help.github.com/articles/connecting-to-github-with-ssh/)).
