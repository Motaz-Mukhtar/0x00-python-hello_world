#!/usr/bin/python3
if __name__ == "__main__":
    import sys
num = 1
length = len(sys.argv) - 1

if length == 1:
    print("{:d} argument:".format(length))
elif len(sys.argv) == 0:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(length))

for i in range(length):
    print("{:d}: {}".format(num, sys.argv[num]))
    num += 1
