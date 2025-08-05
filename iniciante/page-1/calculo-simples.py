def main():
    id_1, qtd_1, value_1 = map(float, input().split())
    id_2, qtd_2, value_2 = map(float, input().split())

    total_1 = (qtd_1 * value_1)
    total_2 = (qtd_2 * value_2)
    total = total_1 + total_2

    print(f"VALOR A PAGAR: R$ {total:.2f}")

    return 0

if __name__ == "__main__":
    main()