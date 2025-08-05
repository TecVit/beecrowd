def main():
  n = int(input())

  for i in range(n):
    x = int(input())
    r = ''

    if x == 0:
      print("NULL")
      continue

    if x % 2 == 0:
      r += 'EVEN '
    else:
      r += 'ODD '

    if x > 0:
      r += "POSITIVE"
    elif x < 0:
      r += "NEGATIVE"

    print(r)

  return 0

if __name__ == "__main__":
  main()