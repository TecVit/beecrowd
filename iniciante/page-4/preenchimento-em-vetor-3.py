def main():
  x = float(input())
  n = 100
  v = [x]

  for i in range(1, n):
    v.append(x / 2)
    x /= 2
  
  for i in range(n):
    print(f"N[{i}] = {v[i]:.4f}")

  return 0

if __name__ == "__main__":
  main()