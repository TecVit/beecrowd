def main():
    a = float(input())
    pa = 3.5

    b = float(input())
    pb = 7.5

    m = ((a * pa) + (b * pb)) / (pa + pb)

    print(f"MEDIA = {m:.5f}")

    return 0

if __name__ == "__main__":
    main()