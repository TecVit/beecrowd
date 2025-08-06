def main():
  c, s = 0, 0

  while True:

    if c == 2:
      print(f"media = {(s / 2):.2f}")
      return 0
    
    x = float(input())

    if x >= 0.00 and x <= 10.00:
      s += x
      c += 1
    else:
      print("nota invalida")

if __name__ == "__main__":
  main()