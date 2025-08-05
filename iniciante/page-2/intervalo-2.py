def main():
  a, b = 10, 20
  n = int(input())

  in_, out_ = 0, 0

  for _ in range(n):
    x = int(input())
    if x >= a and x <= b:
      in_ += 1
    else:
      out_ += 1

  print(f"{in_} in")
  print(f"{out_} out")

  return 0

if __name__ == "__main__":
  main()