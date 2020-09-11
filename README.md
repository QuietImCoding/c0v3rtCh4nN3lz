# c0v3rtCh4nN3lz

An agglomeration of weird covert channel scripts I write for my intro to covert channels class. 

Some of these were written for fun and some of them were written for homework! See if you can guess which is which ¯\_(ツ)_/¯

## A Brief Description of the Folders Herein ##

* nospace - encodes information in zero-width spaces. won't look like it's working in your terminal (probably), but try pasting it into your browser!
* tabspace - encodes information in whitespace at the end of lines in a file. the code is pretty similar to nospace, but I think nospace is cooler
* tmptalk - transmits information _within_ a computer by modulating files in the /tmp directory. you'll need to run it in read mode before you run it in write mode or you'll have to manually clean up desynchronization artifacts! consider yourself warned :) 

