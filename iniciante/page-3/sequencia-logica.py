def main():
  n = int(input())

  for i in range(1, n + 1):
    print(i, (i ** 2), (i ** 3))
    print(i, (i ** 2) + 1, (i ** 3) + 1)

  return 0

if __name__ == "__main__":
  main()