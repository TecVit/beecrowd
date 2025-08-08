def main():
  n = 15
  pares, impares = [], []

  for i in range(n):
    x = int(input())
    
    if x % 2 == 0:
      pares.append(x)
    else:
      impares.append(x)

    if len(pares) == 5:
      for j in range(5):
        print(f"par[{j}] = {pares[j]}")
      pares = []
    
    if len(impares) == 5:
      for j in range(5):
        print(f"impar[{j}] = {impares[j]}")
      impares = []
  
  if len(impares) > 0:
    for i in range(len(impares)):
      print(f"impar[{i}] = {impares[i]}")
  
  if len(pares) > 0:
    for i in range(len(pares)):
      print(f"par[{i}] = {pares[i]}")
      
  return 0

if __name__ == "__main__":
  main()