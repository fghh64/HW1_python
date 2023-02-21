k = int(input('макс. кол-во котлет в сковородке: '))
m = int(input('минуты обжарки с каждой стороны: '))
n = int(input('котлеты: '))
if (k == n):
    print ((n//k)*2*m)
elif (k/n == 2/3):
    print ((n//k*2*m)-m)
else:
    print ((n//k+1)*2*m)