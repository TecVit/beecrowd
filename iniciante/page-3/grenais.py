def main():
  qtd = 0
  pontos_inter, pontos_gremio, empates = 0, 0, 0

  try:
    while True:
      inter, gremio = map(int, input().split())
      escolha = int(input("Novo grenal (1-sim 2-nao)\n"))

      if inter > gremio:
        pontos_inter += 1
      elif gremio > inter:
        pontos_gremio += 1
      else:
        empates += 1

      qtd += 1

      if escolha == 2:
        print(f"{qtd} grenais")
        print(f"Inter:{pontos_inter}")
        print(f"Gremio:{pontos_gremio}")
        print(f"Empates:{empates}")
        
        if pontos_inter > pontos_gremio:
          print(f"Inter venceu mais")
        elif pontos_gremio > pontos_inter:
          print(f"Gremio venceu mais")
        else:
          print(f"Nao houve vencedor")
  except:
    return 0

if __name__ == "__main__":
  main()