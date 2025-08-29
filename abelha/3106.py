def main():
  n = int(input())
  l = list(map(int, input().split()))

  s = 0

  for x in l:
    s += x // 3

  print(s * 3)

  return 0

if __name__ == "__main__":
  main()