def main():
  salario = float(input())
  aumento = 1

  if salario >= 2000.01:
    aumento += (4 / 100)
  elif salario >= 1200.01:
    aumento += (7 / 100)
  elif salario >= 800.01:
    aumento += (10 / 100)
  elif salario >= 400.01:
    aumento += (12 / 100)
  elif salario >= 0:
    aumento += (15 / 100)

  novo_salario = salario * aumento
  print(f'''Novo salario: {novo_salario:.2f}
Reajuste ganho: {(salario * (aumento - 1)):.2f}
Em percentual: {round((aumento - 1) * 100)} %''')

  return 0

if __name__ == "__main__":
  main()