#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)
i=0
## Iterate through configlist
for x in configlist:
    i = i + 1
    if i%2 == 1:
        print(x.strip(),end="\t")
    else:
        print(x.strip())

## Always close your file
configfile.close()

