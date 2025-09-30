def main():
  while True:
    n = 0

    try:
      n = int(input())
    except:
      return 0
  
    if n <= 0:
      print(f"vai ter copa!")
    else:
      print(f"vai ter duas!")

if __name__ == "__main__":
  main()