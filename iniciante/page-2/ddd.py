def main():
  tabela = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte",
  }

  ddd = int(input())

  if ddd not in tabela:
    print(f"DDD nao cadastrado")
  else:
    print(f"{tabela[ddd]}")

  return 0

if __name__ == "__main__":
  main()