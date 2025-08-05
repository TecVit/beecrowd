def main():
  intervalos = [[0,25], [24.99,50], [49.99,75], [74.99,100]]
  numero = float(input())

  for intervalo in intervalos:
    a, b = intervalo[0], intervalo[1]

    if numero >= a and numero <= b:
      r = ''
      
      if ((a + 0.01) % 5) == 0:
        
        r += f"({round(a)},"
      else:
        r += f"[{a},"

      if ((b + 0.01) % 5) == 0:
        r += f"{round(b)})" 
      else:
        r += f"{b}]"

      print(f"Intervalo {r}")

      return 0
  
  print(f"Fora de intervalo")

  return 0

if __name__ == "__main__":
  main()