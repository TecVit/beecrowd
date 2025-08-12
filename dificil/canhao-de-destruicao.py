def main():
  chumbos_disponiveis = int(input())
  chumbos = []

  for i in range(chumbos_disponiveis):
    poder, peso = map(int, input().split())
    chumbos.append((poder, peso))

  carga = int(input())
  resistencia = int(input())

  dp = [[0] * (carga + 1) for _ in range(chumbos_disponiveis + 1)]

  for i in range(1, chumbos_disponiveis + 1):
    poder, peso = chumbos[i-1]
    for w in range(carga + 1):
      dp[i][w] = dp[i-1][w]
      if peso <= w:
        dp[i][w] = max(dp[i][w], dp[i - 1][w - peso] + poder)
  
  maximo_dano = dp[chumbos_disponiveis][carga]
  
  if maximo_dano >= resistencia:
    print("Missao completada com sucesso")
  else:
    print("Falha na missao")
  
  return 0

if __name__ == "__main__":
  n = int(input())
  for i in range(n):
    main()