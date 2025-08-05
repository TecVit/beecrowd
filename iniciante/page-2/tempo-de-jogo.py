def main():
  hi, hf= map(int, input().split())

  si = hi * 3600
  sf = hf * 3600
  
  s = sf - si
  
  h = s // 3600
  s %= 3600

  if hf - hi <= 0:
    h += 24

  print(f"O JOGO DUROU {h} HORA(S)")

  return 0

if __name__ == "__main__":
  main()