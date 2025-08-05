def main():
  list_ = list(map(float, input().split()))
  list_.sort(reverse=True)
  
  a, b, c = list_[0], list_[1], list_[2]

  if a >= b + c:
    print(f"NAO FORMA TRIANGULO")
    return 0
  
  if (a ** 2) == (b ** 2) + (c ** 2):
    print(f"TRIANGULO RETANGULO")
  if (a ** 2) > (b ** 2) + (c ** 2):
    print(f"TRIANGULO OBTUSANGULO")
  if (a ** 2) < (b ** 2) + (c ** 2):
    print(f"TRIANGULO ACUTANGULO")
  if a == b and b == c:
    print(f"TRIANGULO EQUILATERO")
  if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
    print(f"TRIANGULO ISOSCELES")

  return 0

if __name__ == "__main__":
    main()