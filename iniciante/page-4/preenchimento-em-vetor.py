def main():
  x = int(input())
  n = 10
  v = [x]

  for i in range(1, n):
    v.append(v[i-1] * 2)
  
  for i in range(n):
    print(f"N[{i}] = {v[i]}")

  return 0

if __name__ == "__main__":
  main()