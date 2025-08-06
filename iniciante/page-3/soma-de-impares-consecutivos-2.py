def main():
  n = int(input())
  
  for i in range(n):
    x, y = map(int, input().split())
    s = sum([x for x in range(min(x, y) + 1, max(x, y), 1) if x % 2 != 0])
    print(s)

  return 0

if __name__ == "__main__":
  main()