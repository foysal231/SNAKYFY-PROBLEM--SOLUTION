a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a+b+c+d) % 2 == 0 or a==b==c==d or (a == c or a==c+1 or a==c-1) and (b==d or b==d+1 or b==d-1):
    print('YES')
else:
    print('NO')