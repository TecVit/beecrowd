def sortSimple(arr):

  if len(arr) < 2:
    return arr
  
  pivo = arr[0]

  mn = [x for x in arr if x < pivo]
  ig = [x for x in arr if x == pivo]
  mr = [x for x in arr if x > pivo]

  return sortSimple(mn) + ig + sortSimple(mr)

def main():
  list_ = list(map(int, input().split()))
  sorted_ = sortSimple(list_)

  for x in sorted_:
    print(x)
  
  print()
  
  for x in list_:
    print(x)

  return 0

if __name__ == "__main__":
  main()