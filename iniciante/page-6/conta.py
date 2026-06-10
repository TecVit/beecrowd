def main():
  c = int(input())

  for _ in range(c):
    n = int(input())
    l = 0

    for i in range(n):
      if i % 2 == 0:
        l += 1
      else:
        l += -1
    
    print(l)
  
  return 0

if __name__ == "__main__":
  main()