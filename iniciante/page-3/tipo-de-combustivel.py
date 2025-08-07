def main():
  gs = {
    1: "Alcool",
    2: "Gasolina",
    3: "Diesel",
  }

  ts = {
    "Alcool": 0,
    "Gasolina": 0,
    "Diesel": 0,
  }
  
  while True:
    n = int(input())
    if n == 4:
      break
    if n not in gs:
      continue

    ts[gs[n]] += 1

  print("MUITO OBRIGADO")
  for key in ts.keys():
    print(f"{key}: {ts[key]}")

  return 0

main()