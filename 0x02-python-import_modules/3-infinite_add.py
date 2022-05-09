#!/usr/bin/python3
import sys
if __name__ == "__main__":
    la = len(sys.argv)
    i = 1
    res = 0
    if (la == 2):
        print(f"{sys.argv[1]}")
    elif (la > 1):
        for x in range(1, la):
            res += int(sys.argv[i])
            i = i + 1
        print(f"{res}")
    else:
        print("0")
