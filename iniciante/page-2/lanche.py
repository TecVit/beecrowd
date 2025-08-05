def main():
  tabela = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,
  }

  codigo, quantidade = map(int, input().split())
  total = quantidade * tabela[codigo]
  print(f"Total: R$ {total:.2f}")

  return 0

if __name__ == "__main__":
  main()