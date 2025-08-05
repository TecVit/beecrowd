SECONDS_DAY = 86400
SECONDS_HOUR = 3600
SECONDS_MINUTE = 60

def main():
  _, di = map(str, input().split())
  di = int(di)
  hi, _, mi, _, si = map(str, input().split())
  hi, mi, si = int(hi), int(mi), int(si)
  
  _, df = map(str, input().split())
  df = int(df)
  hf, _, mf, _, sf = map(str, input().split())
  hf, mf, sf = int(hf), int(mf), int(sf)

  ti = (di * SECONDS_DAY) + (hi * SECONDS_HOUR) + (mi * SECONDS_MINUTE) + si
  tf = (df * SECONDS_DAY) + (hf * SECONDS_HOUR) + (mf * SECONDS_MINUTE) + sf

  t = tf - ti
  
  w = t // SECONDS_DAY
  t = t % SECONDS_DAY

  x = t // SECONDS_HOUR
  t = t % SECONDS_HOUR

  y = t // SECONDS_MINUTE
  t = t % SECONDS_MINUTE

  z = t

  print(f'''{w} dia(s)
{x} hora(s)
{y} minuto(s)
{z} segundo(s)''')

  return 0

if __name__ == "__main__":
  main()