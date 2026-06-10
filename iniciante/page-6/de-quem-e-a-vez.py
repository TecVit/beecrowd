def main():
  n = int(input())

  for i in range(n):
    jogador1, escolha1, jogador2, escolha2 = input().split()
    numero1, numero2 = map(int, input().split())

    soma = numero1 + numero2
    resultado = "PAR" if soma % 2 == 0 else "IMPAR"

    if escolha1 == resultado:
      print(jogador1)
    else:
      print(jogador2)
    
  return 0

if __name__ == "__main__":
  main()