def main():
  v = float(input())
  
  c_100, c_50, c_20, c_10, c_5, c_2, c_1 = 0, 0, 0, 0, 0, 0, 0
  m_50, m_25, m_10, m_5, m_1 = 0, 0, 0, 0, 0

  while v > 0:
    v = round(v, 2)

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
    elif v - 1 >= 0:
      v -= 1
      c_1 += 1
    elif v - 0.5 >= 0:
      v -= 0.5
      m_50 += 1
    elif v - 0.25 >= 0:
      v -= 0.25
      m_25 += 1
    elif v - 0.10 >= 0:
      v -= 0.10
      m_10 += 1
    elif v - 0.05 >= 0:
      v -= 0.05
      m_5 += 1
    elif v - 0.01 >= 0:
      v -= 0.01
      m_1 += 1
    else:
      break
  
  print(f'''NOTAS:
{c_100} nota(s) de R$ 100.00
{c_50} nota(s) de R$ 50.00
{c_20} nota(s) de R$ 20.00
{c_10} nota(s) de R$ 10.00
{c_5} nota(s) de R$ 5.00
{c_2} nota(s) de R$ 2.00
MOEDAS:
{c_1} moeda(s) de R$ 1.00
{m_50} moeda(s) de R$ 0.50
{m_25} moeda(s) de R$ 0.25
{m_10} moeda(s) de R$ 0.10
{m_5} moeda(s) de R$ 0.05
{m_1} moeda(s) de R$ 0.01''')

  return 0

if __name__ == "__main__":
  main()