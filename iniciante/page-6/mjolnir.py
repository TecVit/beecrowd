def main():
    qtd = int(input())

    for _ in range(qtd):
        line = input().strip()

        while not line:
            line = input().strip()

        name, power = line.split()

        print("Y" if name == "Thor" else "N")

if __name__ == "__main__":
    main()