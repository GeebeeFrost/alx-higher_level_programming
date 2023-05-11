#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid = []
    for name in dir(hidden_4):
        if "__" not in name:
            hid.append(name)
    for name in hid:
        print(name)
