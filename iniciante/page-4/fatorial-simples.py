def main():
  n = int(input())

  f = 1

  for i in range(n, 0, -1):
    f *= i

  print(f)

  return 0

if __name__ == "__main__":
  main()