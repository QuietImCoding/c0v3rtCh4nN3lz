## Some /tmp Directory Covert Channels ##

This script works by using a 3 bit switching system as described in class

There are 2 modules usable here, which you can hot-swap in the code.

The first one will transmit the message by creating and deleting 3 files in the /tmp directory called DATA DSR and DRD

The second one (currently in use), will modulate the name of a file called something like mozilla.lol in the tmp directory to send the message. 

You can check out the usage message in the python script by running `python3 tmptalk.py -h`
