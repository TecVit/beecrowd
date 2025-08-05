def main():
  n = 100
  ns = list(int(input()) for _ in range(n))

  print(max(ns))
  print(ns.index(max(ns)) + 1)

  return 0

if __name__ == "__main__":
  main()