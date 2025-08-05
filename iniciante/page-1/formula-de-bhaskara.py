def main():
  a, b, c = map(float, input().split())

  d = (b ** 2) - 4 * a * c
  rd = d ** (1 / 2)

  try:
    if rd < 0:
      return ValueError
    
    r1 = (-b + rd) / (2 * a)
    r2 = (-b - rd) / (2 * a)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
  except:
    print(f"Impossivel calcular")

  return 0

if __name__ == "__main__":
  main()