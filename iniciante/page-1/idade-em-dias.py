def main():
  dias = int(input())

  anos = dias // 365
  dias = dias % 365

  meses = dias // 30
  dias = dias % 30

  print(f"{anos} ano(s)")
  print(f"{meses} mes(es)")
  print(f"{dias} dia(s)")

  return 0

if __name__ == "__main__":
  main()