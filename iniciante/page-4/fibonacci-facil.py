def fibonacci(n):
  if n == 1:
    return [1]
  
  f = [0, 1]
  
  while len(f) < n:
    f.append(f[-1] + f[-2])

  return f

def main():
  n = int(input())
  f = fibonacci(n)

  print(*f)
  
  return 0

if __name__ == "__main__":
  main()