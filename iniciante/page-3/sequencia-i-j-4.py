def formatarNumero(n):
  return int(n) if n == int(n) else n

def main():
  i, j = 0, 1
  c = 1

  while i <= 2:
    print(f"I={formatarNumero(i)} J={formatarNumero(j)}")

    if c == 3:
      i += 0.2
      i = round(i, 1)
      j = 1 + i
      c = 1
    else:
      j += 1
      c += 1

if __name__ == "__main__":
  main()