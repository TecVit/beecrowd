def main():
  n = 12
  m = [[0 for _ in range(n)] for _ in range(n)]
  
  o = str(input())

  for i in range(n):
    for j in range(n):
      m[i][j] = float(input())
  
  s, c = 0, 0
  
  for i in range(n):
    for j in range(i+1, n-1-i):
      s += m[j][i]
      c += 1
  
  if o == "S":
    print(f"{s:.1f}")
  elif o == "M":
    print(f"{(s / c):.1f}")

  return 0

if __name__ == "__main__":
  main()