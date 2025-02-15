i = 2
while(i<=100):
    j= i//2
    isprime = True
    while(j>1):
        if(i%j==0):
            isprime = False
            break
        j-=1
    if isprime:
      print(i)
    i+=1
