#!/usr/bin/env python3

result = ""

for i in "abcdefghijklmnopqrstuvwxyz":
    if i != "e" and i != "q":
        result = result + i

print("{}".format(result))
