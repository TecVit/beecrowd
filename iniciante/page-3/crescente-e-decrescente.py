def main():
  while True:
    x, y = map(int, input().split())
    
    if x == y:
      return 0
    
    if x < y:
      print("Crescente")
    else:
      print("Decrescente") 

  return 0

if __name__ == "__main__":
  main()