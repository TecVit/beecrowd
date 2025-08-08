def main():
  x = int(input())

  y = int(input())
  while y <= x:
    y = int(input())

  s, c = 0, 0
  while s < y:
    s += x + c
    c += 1
  
  print(c)

  return 0

if __name__ == "__main__":
  main()