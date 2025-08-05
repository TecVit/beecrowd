def main():
  x, y = int(input()), int(input())
  print(sum([i for i in range(min(x, y) + 1, max(x, y), 1) if i % 2 != 0]))

  return 0

if __name__ == "__main__":
  main()