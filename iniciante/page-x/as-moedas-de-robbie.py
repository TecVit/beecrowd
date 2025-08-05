def isPrime(number):
  if number <= 1:
    return False
  
  for x in range(2, int(number ** (1 / 2)) + 1):
    if number % x == 0:
      return False
  return True

def main():

  while True:
    m = 0
    
    try:
      m = int(input())
    except:
      return 0
    
    ms = list(int(input()) for _ in range(m))

    n = int(input())

    s = 0
    for i in range(m - 1, -1, -n):
      s += ms[i]

    if isPrime(s):
      print(f"You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
      print(f"Bad boy! I’ll hit you.")

if __name__ == "__main__":
  main()