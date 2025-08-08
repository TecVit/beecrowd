def main():
  s = 0

  for i in range(1, 100 + 1):
    s += 1 / i

  print(f"{s:.2f}")

  return 0

if __name__ == "__main__":
  main()