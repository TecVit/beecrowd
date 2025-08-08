def main():
  n = int(input())

  m = [[3 for _ in range(n)] for _ in range(n)]
  
  for i in range(n):
    m[i][i] = 1
    m[n-1-i][i] = 2
  
  for r in m:
    for k in r:
      print(k, end="")
    print()
    
  return 0

if __name__ == "__main__":
  try:
    while True:
      main()
  except:
    pass