#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv)
    argc = length - 1
    print("{} {}{}".format(
        argc, ("argument" if argc == 1 else "arguments"),
        ("." if argc < 1 else ":")))
    if argc > 0:
        for i in range(1, length):
            print("{}: {}".format((i), argv[i]))
