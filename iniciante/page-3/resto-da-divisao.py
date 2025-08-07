def main():
  x = int(input())
  y = int(input())

  mn = min(x, y)
  mr = max(x, y)

  for i in range(mn + 1, mr):
    if i % 5 == 2 or i % 5 == 3:
      print(i)

  return 0

if __name__ == "__main__":
  main()