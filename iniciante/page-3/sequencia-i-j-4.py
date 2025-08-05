def format_num(n):
  n = round(n, 1)
  if n.is_integer():
    return str(int(n))
  return str(n)

def main():
  i, j = 0, 1
  c = 1

  while i <= 2:
    print(f"I={format_num(i)} J={format_num(j)}")

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