def main():
  s, c = 0, 1

  for i in range(1, 39 + 1, 2):
    s += (i / c)
    c *= 2

  print(f"{s:.2f}")

  return 0

if __name__ == "__main__":
  main()