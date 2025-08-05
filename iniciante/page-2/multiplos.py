def main():
  a, b = map(int, input().split())

  if max(a, b) % min(a, b) == 0:
    print(f"Sao Multiplos")
  else:
    print(f"Nao sao Multiplos")

  return 0

if __name__ == "__main__":
    main()