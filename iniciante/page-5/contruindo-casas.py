def main():
  a, b, c = map(int, input().split())
  l = ((a * b * 100) / c) ** (1 / 2)

  print(int(l))

  return 0

if __name__ == "__main__":
  try:
    while True:
      main()
  except:
    pass