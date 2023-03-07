#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('A') and ord(c) <= ord('z'):
        for i in range(ord('a'), ord('z') + 1):
            if c == chr(i):
                return True
        return False
