#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    output = 0
    for i in range(1, count):
        output += int(sys.argv[i])
    print('{}'.format(output))
