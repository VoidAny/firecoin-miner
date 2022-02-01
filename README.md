Firecoin Miner
==============

This program was designed to aid in the collection of a digital currency called "Firecoin".

What is Firecoin?
-----------------

Firecoin is a digital currency that is run by a Discord bot on [my friend's Discord server](https://discord.gg/BFVFcaQj6k). It is able to be collected by typing `/mine` into any chat. It can also be traded among users. You can also buy firecoin at a rate of $2 per coin. There is no way to exchange Firecoin to any other currency. 

What does this program do?
--------------------------

This program is designed to periodicly type `/mine` and enter into the chat to obtain Firecoin in an afk manner.

How does it work?
-----------------

This program works by using the pynput library to input text into into Discord. In simpler terms, the program pretends to be the user typing on the keyboard. 

Downsides
---------

The biggest draw back to this program is that it requires you to have the Discord window in focus and be on the correct server/channel. The reason for this is that the program simply types `/mine` and is unable to tell what window is being used.

How to nullify the downside and gain UNLIMITED FIRECOINs
--------------------------------------------------------

The problem of having to constatly have Discord in focus can be fixed by simply running the miner and Discord in a virtual machine. A virtual machine (VM for short) is like a sperate computer that runs on your actual computer. This means that it has its own virtual keyboard. 

In order to get a VM, I would recommend that you use [Virtual Box](https://www.virtualbox.org/) as the virtualization software and [Ubuntu](https://ubuntu.com/download/desktop) (if you are new to this) or [Debian](https://www.debian.org/distrib/) (if you know a fair amount about linux) as your guest os. 

Install
=======

The easy way
------------

If you are on linux:

First, get the source code:

`git clone https://github.com/Dabbing-Guy/firecoin-miner`

Then, go into the source directory:

`cd firecoin-miner`

To install dependencies:

`make`

To install: 

`sudo make install`

Then you can run it by using `fireminer` any where on the system.

If you ever want to unintall, simply cd into the source directory:

`cd firecoin-miner`

Then run:

`sudo make uninstall`

If you are using another os, I recommend using and installing this in a Linux VM.

The no install way
------------------

You can use this program with out installing it by simply installing the dependencies with:

`pip3 install -r requirements.txt`

then run it with: 

`./miner.py`

If it is not installed, then it can only be ran while you are in this directory.

Improvements over v1
====================

v1 of this project can be found [here](https://gist.github.com/Dabbing-Guy/965a014367805350b65358383e60a8c7). 

- Random amount of time between each `/mine` to help with avoiding bot detection and bans
- Increased ablity to configure due to extracting literals to easy to edit variables
- Comes with a license
- Easier to install due to makefile and requirements.txt for pip
- You can pass `--help` to it now
- and probably more...
