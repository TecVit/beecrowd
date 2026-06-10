def main():
  gritos = 0
  soma = 0

  while gritos < 3:
    entrada = str(input())

    if entrada == "caw caw":
      print(soma)
      soma = 0
      gritos += 1

      continue

    if entrada[2] == "*":
      soma += 1
    if entrada[1] == "*":
      soma += 2
    if entrada[0] == "*":
      soma += 4

  return 0

if __name__ == "__main__":
  main()