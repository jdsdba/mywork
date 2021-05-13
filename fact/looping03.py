#!/usr/bin/env python3
#this library allows us to generate UUID values.
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")
nums = []
# range is required because an int cannot be looped
for rando in range(howmany):
    newid = uuid.uuid4()
    if newid in nums:
        print(f'{newid} already exists')
    nums.append(newid)
    #print( newid )
    #print(nums)

