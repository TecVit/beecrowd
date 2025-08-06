def main():
  c, s = 0, 0

  while True:

    if c == 2:
      print(f"media = {(s / 2):.2f}")
      e = 0
      while e != 1 and e != 2:
        e = int(input("novo calculo (1-sim 2-nao)"))

      if e == 2:
        return 0
      else:
        c, s = 0, 0
        continue

    x = float(input())

    if x >= 0.00 and x <= 10.00:
      s += x
      c += 1
    else:
      print("nota invalida")

if __name__ == "__main__":
  main()