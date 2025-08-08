def main():
  n = int(input())

  for i in range(n):
    x, y = map(int, input().split())
    s = 0

    for i in range(x, x + (2 * y)):
      if i % 2 != 0:
        s += i

    print(s)

  return 0

if __name__ == "__main__":
  main()