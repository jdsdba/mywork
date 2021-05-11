#!/usr/bin/env python3

message = 'Game of Thrones episode? '

# wrap connection in a float() to accept decimals as numbers
episode = int(input(message))

# if input value was higher or equal to 25
if episode == 1:
    cnt = 1
elif episode == 2:
    cnt = 4
elif episode >= 2:
    cnt = episode * 2
else:
    cnt = 32

print(f"{cnt} people died in espisode {episode}")
