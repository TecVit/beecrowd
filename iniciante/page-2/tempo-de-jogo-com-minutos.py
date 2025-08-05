def main():
  hi, mi, hf, mf = map(int, input().split())

  si = hi * 3600 + mi * 60
  sf = hf * 3600 + mf * 60
  
  s = sf - si
  
  h = s // 3600
  s %= 3600

  m = s // 60
  s %= 60

  if hf - hi <= 0 and mf - mi <= 0:
    h += 24

  print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")

  return 0

if __name__ == "__main__":
  main()