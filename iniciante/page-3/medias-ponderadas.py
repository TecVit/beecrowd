def main():
  n = int(input())

  for i in range(n):
    n1, n2, n3 = map(float, input().split())
    m = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)
    print(f"{m:.1f}")

  return 0

if __name__ == "__main__":
  main()