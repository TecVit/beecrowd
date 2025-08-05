def main():
  n = int(input())

  for i in range(n):
    x, y = map(int, input().split())

    try:
      print(f"{(x / y):.1f}")
    except:
      print(f"divisao impossivel")

  return 0

if __name__ == "__main__":
  main()