def main():
  numeros = list(float(input()) for _ in range(5))

  pares = len([numero for numero in numeros if numero % 2 == 0])
  impares = len([numero for numero in numeros if numero % 2 != 0])
  positivos = len([numero for numero in numeros if numero > 0])
  negativos = len([numero for numero in numeros if numero < 0])

  print(f"{pares} valor(es) par(es)")
  print(f"{impares} valor(es) impar(es)")
  print(f"{positivos} valor(es) positivo(s)")
  print(f"{negativos} valor(es) negativo(s)")

  return 0

if __name__ == "__main__":
  main()