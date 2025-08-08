def main():
  list_ = [int(x) for x in input().split() if int(x) > 0]
  
  a, n = list_[0], list_[1]
  s = 0

  for i in range(0, n):
    s += (a + i)  
  
  print(s)

  return 0

if __name__ == "__main__":
  main()