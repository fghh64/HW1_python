n = int(input())

if  (n%10==2 or n%10==3 or n%10==4) and n//10!=1:
    print('коровы')
elif n%10==1 and n!=11:
    print('корова')
else:
    print('коров')