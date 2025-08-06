def main():
  n, m, k = map(int, input().split())

  menor_g = float('inf')
  
  for a in range(1, k + 1):
    b = k // a
    if b == 0:
      continue
    
    comprimento = (n + a - 1) // a
    largura = (m + b - 1) // b
    g = max(comprimento, largura)
    menor_g = min(menor_g, g)

  print(menor_g)

  return 0

if __name__ == "__main__":
  main()