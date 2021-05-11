#!/usr/bin/env python3
ipcheck = input("Apply an IP address: ") # this line now prompts the user for input
splitip = ipcheck.split('.')
print(splitip)

if len(splitip) != 4:
        print('Not an IP Address')
# a provided string will test true
elif splitip:
   print("Looks like the IP address was set: " + ipcheck) # indented under if
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else
