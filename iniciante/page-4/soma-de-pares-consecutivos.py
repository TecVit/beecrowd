def main():
  while True:
    x = int(input())
    if x == 0:
      break
    
    s = 0
    for i in range(x, x + (2 * 5)):
      if i % 2 == 0:
        s += i

    print(s)

  return 0

if __name__ == "__main__":
  main()