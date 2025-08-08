def isPrime(n):
  r = int(n ** (1 / 2))

  for i in range(2, r + 1):
    if n % i == 0:
      return False

  return True

def main():
  n = int(input())

  for _ in range(n):
    x = int(input())
    if isPrime(x):
      print(f"{x} eh primo")
    else:
      print(f"{x} nao eh primo")
  
  return 0

if __name__ == "__main__":
  main()