num = int(input('enter the number: '))
isprime = True
for i in range(num//2,1,-1):
    if(num%i==0):
        print(f'{num} is not prime')
        isprime = False
        break
if isprime:
  print('it is prime')
          
