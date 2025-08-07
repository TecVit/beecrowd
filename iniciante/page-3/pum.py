import time

def main():
  n = int(input())

  start = time.time()

  for i in range(1, n * 4, 4):
    print(i, i + 1, i + 2, "PUM")

  end = time.time()
  duration = end - start

  # print(f"Tempo de execução: {duration:.4f} segundos")

if __name__ == "__main__":
  main()