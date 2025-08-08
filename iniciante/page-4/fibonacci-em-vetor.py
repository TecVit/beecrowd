def fibonacci(n):
  if n <= 1:
    return n
  
  f = [0, 1]
  
  while len(f) <= n:
    f.append(f[-1] + f[-2])

  return f[n]

def main():
  n = int(input())
  
  for i in range(n):
    x = int(input())
    f = fibonacci(x)

    print(f"Fib({x}) = {f}")
  
  return 0

if __name__ == "__main__":
  main()