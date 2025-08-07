def main():
  x = int(input())
  y = int(input())

  s = 0

  for i in range(min(x, y), max(x, y) + 1, 1):
    if i % 13 != 0:
      s += i

  print(s)

  return 0

if __name__ == "__main__":
  main()