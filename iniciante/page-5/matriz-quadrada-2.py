def main():
  while True:
    n = int(input())
    if n == 0:
      break
    
    m = [[i + 1 for i in range(n)] for _ in range(n)]
    
    for i in range(n):
      l = m[i]
      p1 = l[:n-i]
      p2 = [i + 1 for i in range(1, n - len(p1) + 1)]
      p2.sort(reverse=True)
      p = p2 + p1
      m[i] = p

    for r in m:
      print(" ".join(f"{num:>3}" for num in r))
    print()
    
  return 0

if __name__ == "__main__":
  try:
    main()
  except:
    pass