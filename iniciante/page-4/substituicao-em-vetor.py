def main():
  v = []

  for i in range(10):
    x = int(input())
    if x <= 0:
      x = 1
    v.append(x)

  for i in range(len(v)):
    x = v[i]
    print(f"X[{i}] = {x}")

  return 0

if __name__ == "__main__":
  main()