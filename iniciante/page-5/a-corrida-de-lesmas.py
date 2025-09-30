def main():
  while True:
    l = 0

    try: 
      l = int(input())
    except:
      return 0

    ls = list(map(int, input().split()))

    if max(ls) >= 20:
      print(3)
    elif max(ls) >= 10:
      print(2)
    elif max(ls) < 10:
      print(1)


if __name__ == "__main__":
  main()