def main():
    a, b, c = map(int, input().split())

    maior_a_b = (a + b + abs(a - b)) / 2
    maior_x_c = (maior_a_b + c + abs(maior_a_b - c)) / 2
    
    print(f"{int(maior_x_c)} eh o maior")

    return 0

if __name__ == "__main__":
    main()