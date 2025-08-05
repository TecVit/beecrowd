def main():
  c = 0

  for _ in range(6):
    n = float(input())
    if n > 0:
      c += 1
  
  print(f"{c} valores positivos")

  return 0

if __name__ == "__main__":
    main()