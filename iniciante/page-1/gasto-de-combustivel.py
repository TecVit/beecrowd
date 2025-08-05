def main():
  h = int(input())
  vm = int(input())
  km = vm * h
  km_l = km / 12

  print(f"{km_l:.3f}")

  return 0

if __name__ == "__main__":
  main()