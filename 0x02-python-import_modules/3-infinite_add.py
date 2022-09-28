#!/usr/bin/python3
if __name__ == "__main__":
    import sys
length = len(sys.argv)
num_sum = 0
i = 1

while i < length:
    num_sum += int(sys.argv[i])
    i += 1
print(num_sum)
