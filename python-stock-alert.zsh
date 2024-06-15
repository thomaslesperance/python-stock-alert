#!/bin/zsh

# This script runs the python script with the same filename.
# First, make sure you are declaring the right interpreter at the top
# of this file with 'echo $SHELL'. If you get back '/bin/zsh' in the terminal,
# then the very first line of this file must be '#!/bin/zsh'.
# ---
# Be sure to run the following command for the finished
# file to allow you to run it as a script:
# ‘chmod u+x python-script.command’
# ---
# Save this file in a folder that is part of your PATH.
# To verify which directories are in your PATH, use ‘echo $PATH’.
# To add a specific folder (which this .zsh file can be found), do
# this: 'nano ~/.zshrc', then add this to the bottom of .zshrc:
# 'export PATH=$PATH:/path/to/your/directory', then enter 'source ~/.zshrc'
# and verify again with 'echo $PATH'.
# ---
# On MacOS, run script with ‘cmd + space’ to bring up spotlight, then 
# type ‘python-script’ and press 'enter'.
# Good luck! XD

# Zsh script should:
# offer help info
# be added to PATH
# pass CLI arguments to python script

python3 main.py $1 $2 $3 $4
