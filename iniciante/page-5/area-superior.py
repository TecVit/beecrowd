def main():
  n = 4
  m = [[0 for _ in range(n)] for _ in range(n)]
  
  o = str(input())

  for i in range(n):
    for j in range(n):
      m[i][j] = float(input())
  
  s, c = 0, 0
  mx = (n // 2)
  if mx % 2 == 0:
    mx -= 2
  else:
    mx -= 1
  
  for i in range(n):
    for j in range(1+i, n-1-i):
      s += m[i][j]
      c += 1
  
  if o == "S":
    print(f"{s:.1f}")
  elif o == "M":
    print(f"{(s / c):.1f}")

  return 0

if __name__ == "__main__":
  main()