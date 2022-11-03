a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a+b+c+d) % 2 == 0 or a==b==c==d or (a-c) == (b-d):
    print('YES')
else:
    print('NO')