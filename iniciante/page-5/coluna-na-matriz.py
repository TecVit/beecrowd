def main():
  n = 12
  c = int(input())
  t = str(input())

  m = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      m[i][j] = float(input())
  
  if t == "S":
    s = 0
    for i in range(n):
      s += m[i][c]
    print(f"{s:.1f}")
  elif t == "M":
    s, l = 0, 0
    for i in range(n):
      s += m[i][c]
      l += 1
    print(f"{(s / l):.1f}")

  return 0

if __name__ == "__main__":
  main()