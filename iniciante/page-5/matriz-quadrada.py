def main():
  while True:
    n = int(input())
    if n == 0:
      break
    
    m = [[1 for _ in range(n)] for _ in range(n)]
    
    c = 1

    while c <= (n - 2):
      for i in range(c, n - c):
        for j in range(c, n - c):
          m[i][j] = c + 1
      c += 1

    
    for r in m:
      print(" ".join(f"{num:>3}" for num in r))
    print()
    
  return 0

if __name__ == "__main__":
  try:
    main()
  except:
    pass