reverse = 0
num = int(input('enter the number: '))
while(num>0):
    digit = num%10
    reverse = reverse*10 + digit
    num//=10
print(f' reverse : {reverse}')
