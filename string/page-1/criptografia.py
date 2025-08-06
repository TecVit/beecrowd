def main():
  n = int(input())

  for _ in range(n):
    linha = input()

    passo1 = ''
    for c in linha:
      if c.isalpha():
        passo1 += chr(ord(c) + 3)
      else:
        passo1 += c

    # 2ª Passada: inverter string
    passo2 = passo1[::-1]

    # 3ª Passada: deslocar -1 a partir da metade truncada
    metade = len(passo2) // 2
    passo3 = ''

    for i in range(len(passo2)):
      if i >= metade:
        passo3 += chr(ord(passo2[i]) - 1)
      else:
        passo3 += passo2[i]

    print(passo3)

if __name__ == "__main__":
  main()