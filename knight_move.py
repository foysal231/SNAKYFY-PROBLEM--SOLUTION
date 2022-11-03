a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (c == a + 1 or c == a - 1) and (d== b - 2 or d== b+ 2):
  print ("YES")
elif (d== b+ 1 or d==b- 1) and (c == a - 2 or c== a + 2):
  print ("YES")
else:
    print('NO')