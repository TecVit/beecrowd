def main():
  n = int(input())

  for x in range(1, n + 1):
    if x % 2 != 0:
      continue
    print(f"{x}^2 = {x ** 2}")

  return 0

if __name__ == "__main__":
  main()