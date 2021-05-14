#!/usr/bin/env python3
import urllib.request
import re

print("Where should we search?")
url = input()

while True:
    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase [enter to exit]:")
    searchFor = input()
    if not searchFor:
        print ('Done!')
        exit()

    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    #if re.search(searchFor, searchMe):
    matches = re.findall(searchFor, searchMe)

    if matches:
        print(f"Found a {len(matches)} matches!")
    else:
        print("No match!")

