def main():
    a, b, c = map(int, input().split())

    if b < a and c >= b:
        print(":)")
    elif b > a and c <= b:
        print(":(")
    elif b > a and c > b:
        if (c - b) >= (b - a):
            print(":)")
        else:
            print(":(")
    elif b < a and c < b:
        if (b - c) < (a - b):
            print(":)")
        else:
            print(":(")
    elif a == b:
        if c > b:
            print(":)")
        else:
            print(":(")

    return 0

if __name__ == "__main__":
    main()