n = int(input())

sums = [0, 0, 0]

for _ in range(n):
    x, y, z = map(int, input().split())
    sums[0] += x
    sums[1] += y
    sums[2] += z

if  sums == [0,0,0]:
    print("YES")
else:
    print("NO")