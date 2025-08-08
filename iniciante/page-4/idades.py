def main():
  xs = []

  while True:
    x = int(input())
    if x > 0:
      xs.append(x)
    else:
      break

  print(f"{(sum(xs) / len(xs)):.2f}")
  
  return 0

if __name__ == "__main__":
  main()