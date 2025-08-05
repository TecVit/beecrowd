def main():
  numeros = list(float(input()) for _ in range(6))

  positivos = [numero for numero in numeros if numero > 0]
  media = sum(positivos) / len(positivos)

  print(f"{len(positivos)} valores positivos")
  print(f"{media:.1f}")

  return 0

if __name__ == "__main__":
  main()