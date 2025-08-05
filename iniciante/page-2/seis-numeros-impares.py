def main():
  x = int(input())

  for i in range(x, x + 12, 1):
    if i % 2 != 0:
      print(i)

  return 0

if __name__ == "__main__":
  main()