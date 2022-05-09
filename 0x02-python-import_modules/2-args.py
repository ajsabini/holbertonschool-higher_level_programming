#!/usr/bin/python3
import sys
if __name__ == "__main__":
    la = len(sys.argv)
    i = 1
    if (la == 1):
        print("0 arguments.")
    elif (la == 2):
        print(f"1 argument:\n{1}: {sys.argv[1]}")
    else:
        print(f"{la - 1} arguments:")
        for x in range(1, la):
            print(f"{i}: {sys.argv[i]}")
            i = i +1
