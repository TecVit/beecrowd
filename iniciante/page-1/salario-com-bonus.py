def main():
  n = str(input())
  s = float(input())
  v = float(input())

  t = s + (v * 0.15)

  print(f"TOTAL = R$ {t:.2f}")

  return 0

if __name__ == "__main__":
  main()