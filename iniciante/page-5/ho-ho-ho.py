def main():
  n = int(input())

  for i in range(n):
    if (i + 1) == n:
      print("Ho!")
    else:
      print("Ho", end=" ")

  return 0

if __name__ == "__main__":
  main()