# Using this Covert Channel #

This should be a fairly easy program to use. 
If you run `python3 tabspace.py`, the usage message should explain it.

If you want to decode the text from a file, you run the script with 1 argument, and if you want to encode text, you put the carrier file first and the message file second. 
I suspect that the script is *fairly* robust when it comes to input handling, but I don't think it's perfect.

In order to quickly get up and running, I created a version of the original file with no text encoded called innocuous.txt. There is the same message as the original file contained in secretmsg.txt.
You can get a similar output to the original running `python3 tabspace.py innocuous.txt secretmsg.txt`.
If you pipe this output to a file called welcome2.txt, you should be able to get the original output back, by running `python3 tabspace.py welcome2.txt`

Have fun running this, and if you have any questions feel free to email me @ **REDACTED**
