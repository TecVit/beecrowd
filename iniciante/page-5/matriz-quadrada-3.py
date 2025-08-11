def main():
  while True:
    n = int(input())
    if n == 0:
      break
    
    m = [[0 for _ in range(n)] for _ in range(n)]
    mr = float("-inf")
    
    for i in range(n):
      for j in range(n):
        x = 2 ** (i+j)
        m[i][j] = x
        mr = max(mr, x)

    t = len(str(mr))
    for r in m:
      print(" ".join(f"{num:>{t}}" for num in r))
    print()
    
  return 0

if __name__ == "__main__":
  try:
    main()
  except:
    pass