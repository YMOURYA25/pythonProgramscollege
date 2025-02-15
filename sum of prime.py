i = 2
sum = 0
while(i<=10):
    j= i//2
    isprime = True
    while(j>1):
        if(i%j==0):
            isprime = False
            break
        j-=1
    if isprime:
      sum+=i
    i+=1
print(sum)
