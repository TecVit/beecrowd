from collections import deque

def main():
  t = int(input())
  
  for _ in range(t):
    n, k, s = map(int, input().split())
    
    dq = deque()
    soma = 0
    
    prev = s
    window = []

    for i in range(n):
      if i == 0:
        val = s
      else:
        val = (prev * 1103515245 + 12345) % 2147483648
        prev = val
      
      while dq and window[dq[-1]] <= val:
        dq.pop()

      dq.append(len(window))
      window.append(val)
      
      if dq[0] <= len(window) - k - 1:
        dq.popleft()
      
      if i >= k - 1:
        soma += window[dq[0]]
        window.pop(0)
        dq = deque([idx - 1 for idx in dq])
    
    print(soma)

if __name__ == "__main__":
  main()