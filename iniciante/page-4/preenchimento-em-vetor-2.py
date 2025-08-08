def main():
  t = int(input())
  n = 1000
  v = []

  c = 0
  for i in range(n):
    if c == t:
      c = 0
    v.append(c)
    c += 1
  
  for i in range(n):
    print(f"N[{i}] = {v[i]}")

  return 0

if __name__ == "__main__":
  main()