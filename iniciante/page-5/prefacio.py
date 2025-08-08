def main():
  a, b = map(int, input().split())

  q = a // b
  r = a % b
  
  if r < 0:
    r += abs(b)
    q = (a - r) // b

  print(f"{q} {r}")

  return 0

if __name__ == "__main__":
  main()