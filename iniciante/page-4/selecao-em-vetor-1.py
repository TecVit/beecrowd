def main():
  n = 100
  v = []

  for i in range(n):
    x = float(input())
    v.append(x)
  
  for i in range(n):
    if v[i] <= 10:
      print(f"A[{i}] = {v[i]:.1f}")

  return 0

if __name__ == "__main__":
  main()