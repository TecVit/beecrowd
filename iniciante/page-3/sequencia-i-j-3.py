def main():
  i, j, a = 1, 7, 7

  while i <= 9:
    print(f"I={i} J={j}")

    if a - j == 2:
      i += 2
      j = a + 2
      a = j
      continue

    j -= 1

  return 0

if __name__ == "__main__":
  main()