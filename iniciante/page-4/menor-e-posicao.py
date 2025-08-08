def main():
  _ = int(input())
  ns = list(map(int, input().split()))

  print(f"Menor valor: {min(ns)}")
  print(f"Posicao: {ns.index(min(ns))}")
      
  return 0

if __name__ == "__main__":
  main()