num = int(input('enter the number: '))
temp = num
ams = 0
while(temp > 0):
    digit = temp%10
    ams += digit **3
    temp//=10
if ams!=num:
    print('not amstrong')
else:
    print('anstrong')
