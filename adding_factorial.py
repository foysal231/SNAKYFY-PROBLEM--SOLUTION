num = int (input())
fact=1
sum=0
for i in range(num):
    i+=1
    fact*= i
    sum+=fact
print(sum)