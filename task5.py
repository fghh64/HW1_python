a = int(input())
b = int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('No')
else:
    print(-b/a)