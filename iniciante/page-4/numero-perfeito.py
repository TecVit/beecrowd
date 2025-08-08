def main():
  n = int(input())

  for _ in range(n):
    x = int(input())
    xs = []
    i = 1

    while i < x:
      if x % i == 0:
        xs.append(i)
      i += 1

    if sum(xs) == x:
      print(f"{x} eh perfeito")
    else:
      print(f"{x} nao eh perfeito")
  
  return 0

if __name__ == "__main__":
  main()