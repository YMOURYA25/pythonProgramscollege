num = int(input('enter the number: '))
temp = num
sum = 0
while(temp > 0):
    digit = temp%10
    sum += digit
    temp//=10
print(sum)
