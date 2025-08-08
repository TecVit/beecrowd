def main():
  n = 20
  v = [0 for _ in range(n)]

  for i in range(n):
    x = int(input())
    v[n-1-i] = x
  
  for i in range(n):
    print(f"N[{i}] = {v[i]}")

  return 0

if __name__ == "__main__":
  main()