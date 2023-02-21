x = int(input())
n = ''

# X до C
if x < 100 and x >= 90:
    n+='X'
# C
if x<=100 and x>=90:
    n += 'C'
# X до L
if x >= 40 and x <=49:
    n += 'X'
# L
if x>=40 and x < 90:
    n += 'L'
# X после L
if (x-50)//10<4:
    n += 'X'*((x-50)//10)
# X
if x//10 < 4:
    n +='X'*(x//10)
# IX
if x%10==9:
    n += 'IX'
# I до V
if x%10==4:
    n +='I'
# V
if x%10 >= 4 and x%10 <=8:
    n += 'V'
# I после V
if (x-5)%10<4:
    n += 'I'*((x-5)%10)
# I
if x%10 <4:
    n += 'I'*(x%10)

print(n)