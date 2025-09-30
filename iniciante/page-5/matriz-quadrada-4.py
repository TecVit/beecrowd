def main():
  while True:
    n = 0

    try:
      n = int(input())
    except:
      break
    
    if n % 2 == 0:
      break

    m = [[0] * n for _ in range(n)]

    for i in range(n):
      m[i][i] = 2
      m[i][n-1-i] = 3
    
    for i in range(n // 3, n - (n // 3)):
      for j in range(n // 3, n - (n // 3)):
        m[i][j] = 1

    m[n // 2][n // 2] = 4

    for r in m:
      print("".join(str(x) for x in r))
    print()

  return 0

if __name__ == "__main__":
  main()