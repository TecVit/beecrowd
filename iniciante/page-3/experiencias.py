def main():
  n = int(input())

  nomes_das_cobaias = {
    "C": "coelhos",
    "R": "ratos",
    "S": "sapos",
  }

  cobaias = {}
  total = 0
  for i in range(n):
    qtd, tip = map(str, input().split())
    qtd = int(qtd)

    if tip in cobaias:
      cobaias[tip] += qtd
    else:
      cobaias[tip] = qtd
    
    total += qtd
  
  print(f"Total: {total} cobaias")
  for key in cobaias.keys():
    print(f"Total de {nomes_das_cobaias[key]}: {cobaias[key]}")
  
  for key in cobaias.keys():
    print(f"Percentual de {nomes_das_cobaias[key]}: {((cobaias[key] / total) * 100):.2f} %")

  return 0

if __name__ == "__main__":
  main()