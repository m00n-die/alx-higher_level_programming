#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    add_result = 0
    n = len(sys.argv)
    for i in range(1, n):
        add_result += int(sys.argv[i])
    print(add_result)
