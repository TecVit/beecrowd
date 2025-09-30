def main():
  opcoes = {
    "tesoura": {
      "ganha": ["papel", "lagarto"],
      "perde": ["spock", "pedra"],
    },
    "papel": {
      "ganha": ["spock", "pedra"],
      "perde": ["lagarto", "tesoura"],
    },
    "pedra": {
      "ganha": ["lagarto", "tesoura"],
      "perde": ["papel", "spock"],
    },
    "spock": {
      "ganha": ["tesoura", "pedra"],
      "perde": ["lagarto", "papel"],
    },
    "lagarto": {
      "ganha": ["spock", "papel"],
      "perde": ["pedra", "tesoura"],
    },
  }

  n = int(input())

  for i in range(n):
    j1, j2 = map(str, input().lower().split())
    res = "De novo!"

    if j2 in opcoes[j1]["ganha"]:
      res = "Bazinga!"
    elif j1 in opcoes[j2]["ganha"]:
      res = "Raj trapaceou!"
      
    print(f"Caso #{i+1}: {res}")

  return 0

if __name__ == "__main__":
  main()