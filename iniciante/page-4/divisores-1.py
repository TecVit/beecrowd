def main():
  n = int(input())
  i = 1

  while i <= n:
    if n % i == 0:
      print(i)
    i += 1

  return 0

if __name__ == "__main__":
  main()