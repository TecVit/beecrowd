def main():
  i, j = 1, 7

  while i <= 9:
    print(f"I={i} J={j}")

    if j == 5:
      i += 2
      j = 7
      continue

    j -= 1

  return 0

if __name__ == "__main__":
  main()