#!/usr/bin/env python3

# create the string hostname
hostname = ''
while not hostname:
    hostname = input("What value should we set for hostname? ")

# test logic with the `if` statement
# what to do if this statement is found to be true
if hostname.upper() == "MTG":
    print(f"The hostname was found to be {hostname}")

