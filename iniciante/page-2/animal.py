def main():
  teia = {
    "vertebrado": {
      "ave": {
        "carnivoro": "aguia",
        "onivoro": "pomba",
      },
      "mamifero": {
        "onivoro": "homem",
        "herbivoro": "vaca",
      },
    },
    "invertebrado": {
      "inseto": {
        "hematofago": "pulga",
        "herbivoro": "lagarta",
      },
      "anelideo": {
        "hematofago": "sanguessuga",
        "onivoro": "minhoca",
      },
    },
  }

  a = str(input()).strip()
  b = str(input()).strip()
  c = str(input()).strip()

  print(teia[a][b][c])

  return 0

if __name__ == "__main__":
  main()