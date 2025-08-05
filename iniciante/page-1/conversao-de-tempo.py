def main():
  s = int(input())

  horas = s // 3600
  s = s % 3600

  minutos = s // 60
  s = s % 60

  segundos = s

  print(f"{horas}:{minutos}:{segundos}")

  return 0

if __name__ == "__main__":
  main()