Flask_Vagrant_Files
===================

These are the files I use to bootstrap a fresh Flask development evironment on a Ubuntu 32-bit VM. If you have Vagrant installed on your local machine, all you have to do is clone this directory, and run "vagrant up" at the terminal, and you'll have a fresh python development environment with flask ready to go.

Run "vagrant ssh" in the project directory to talk to the VM.

When you install new packages or software to your VM (e.g. "pip install \foobar\" or even a database or anything like that) be sure to append that command to bootstrap.sh, so that when someone else clones your project, they can still just run "vagrant up" and get exactly the same development environment as you have.