def main():
  qtd = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
    0: 6,
  }

  n = int(input())

  for _ in range(n):
    s = str(input()).strip()
    c = 0

    for i in range(len(s)):
      c += qtd[int(s[i])]

    print(f"{c} leds")

  return 0

if __name__ == "__main__":
  main()