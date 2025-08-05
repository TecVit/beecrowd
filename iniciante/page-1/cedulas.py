def main():
  v = int(input())
  c_100, c_50, c_20, c_10, c_5, c_2, c_1 = 0, 0, 0, 0, 0, 0, 0

  print(v)

  while v > 0:
    
    if v - 100 >= 0:
      v -= 100
      c_100 += 1
    elif v - 50 >= 0:
      v -= 50
      c_50 += 1
    elif v - 20 >= 0:
      v -= 20
      c_20 += 1
    elif v - 10 >= 0:
      v -= 10
      c_10 += 1
    elif v - 5 >= 0:
      v -= 5
      c_5 += 1
    elif v - 2 >= 0:
      v -= 2
      c_2 += 1
    else:
      v -= 1
      c_1 += 1
  
  print(f'''{c_100} nota(s) de R$ 100,00
{c_50} nota(s) de R$ 50,00
{c_20} nota(s) de R$ 20,00
{c_10} nota(s) de R$ 10,00
{c_5} nota(s) de R$ 5,00
{c_2} nota(s) de R$ 2,00
{c_1} nota(s) de R$ 1,00''')

  return 0

if __name__ == "__main__":
  main()