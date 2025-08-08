def main():
  while True:
    n = int(input())
    if n == 0:
      return 0

    for i in range(1, n + 1, 1):
      if i == n:
        print(i)
      else:
        print(i, end=" ")

if __name__ == "__main__":
  main()