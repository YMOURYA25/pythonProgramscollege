import array as arr
num= arr.array('i',[1,2,2,3,4])
print(num)
num[0]=0
print(num)
num[2:4]=arr.array('i',[3,4,5])
print(num)
