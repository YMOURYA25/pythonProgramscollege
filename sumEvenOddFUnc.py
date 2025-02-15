def sumEvenAndOdd(len):
    evenSum = 0
    oddSum = 0
    for i in range(1,len+1):
        if(i%2==0):
            evenSum+=i
        else:
            oddSum+=i
    print(evenSum,oddSum)

sumEvenAndOdd(20)
