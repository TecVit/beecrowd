def main():
    a = float(input())
    pa = 2

    b = float(input())
    pb = 3

    c = float(input())
    pc = 5

    m = ((a * pa) + (b * pb) + (c * pc)) / (pa + pb + pc)

    print(f"MEDIA = {m:.1f}")

    return 0

if __name__ == "__main__":
    main()