#!/usr/bin/env python3

myipaddr = ''
while not myipaddr:
    myipaddr = input("Please enter in an IPv4 IP address: ")
print(f"You told me the IPv4 adress is: {myipaddr}", end='!!!\n')

vendorname = ''
while not vendorname:
    vendorname = input("Please enter in the vendor name: ")
print(f"You told me the vendor is: {vendorname}", end='!!!\n')
