
w to create SSH keys

What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

How to use while, until and for loops

How to use if, else, elif and case condition statements

How to use the cut command

What are files and other comparison operators, and how to use them

Requirements

Tasks

0. Create a SSH RSA key pair

mandatory

Read for this task:



Linux and Mac OS users

Windows users

man: ssh-keygen



You will soon have to manage your own servers concept page hosted on remote data centers. We need to set them up with your RSA public key so that you can access them via SSH.



Create a RSA key pair.



Requirements:



Share your public key in your answer file 0-RSA_public_key.pub

Fill the SSH public key field of your intranet profile with the public key you just generated

Keep the private key to yourself in a secure location, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects

If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

SSH and RSA keys will be covered in depth in a later project.



Repo:



GitHub repository: alx-system_engineering-devops

Directory: 0x04-loops_conditions_and_parsing

File: 0-RSA_public_key.pub
