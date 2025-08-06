def main():
  n, m = map(int, input().split())
  
  if min(n, m) <= 0:
    return 0
  
  print(*[x for x in range(min(n, m), max(n, m) + 1, 1)], f"Sum={sum([x for x in range(min(n, m), max(n, m) + 1, 1)])}")

  return 0

if __name__ == "__main__":
  try:
    while True:
      main()
  except:
    pass