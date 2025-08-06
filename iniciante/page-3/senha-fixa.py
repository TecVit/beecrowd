def main():
  while True:
    password = int(input())
    
    if password == 2002:
      print("Acesso Permitido")
      return 0
    else:
      print("Senha Invalida")

if __name__ == "__main__":
  main()