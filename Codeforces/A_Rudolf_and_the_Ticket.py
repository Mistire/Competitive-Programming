t = int(input())

for _ in range(t):
  n, m, k = map(int, input().split())

  b = list(map(int, input().split()))
  c = list(map(int, input().split()))
  

  b.sort()
  c.sort()

  count = 0
  l = 0
  r = m - 1
  while l < n and r >= 0:
    if b[l] + c[r] <= k:
      count += r + 1
      l += 1
    else:
      r -= 1
  print(count)


