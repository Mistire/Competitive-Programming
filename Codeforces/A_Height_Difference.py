t = int(input())
isDiff = True
for _ in range(t):
  col, diff = map(int, input().split())
  arr = list(map(int, input().split()))

  def heightDiff(arr, diff):
    arr.sort()
    l,r = 0, len(arr) - 1
    while l <= r:
      m = (l+r) // 2
      for i in range(r):
        if arr[m] < arr[i] or arr[m] - arr[i] < diff:
          return False
        if arr[m] == arr[i]:
          l = m + 1
          arr[m] = arr[i]
        elif arr[i] != arr[i+1]:
          r = m - 1
          arr[m] = arr[i]
    return True
      
  

  if heightDiff(arr, diff):
    print("YES")
  else:
    print("NO")
    
