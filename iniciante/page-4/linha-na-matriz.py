def main():
  n = 12
  l = int(input())
  t = str(input())

  m = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      m[i][j] = float(input())

  if t == "S":
    print(f"{sum(m[l]):.1f}")
  elif t == "M":
    print(f"{(sum(m[l]) / len(m[l])):.1f}")

  return 0

if __name__ == "__main__":
  main()