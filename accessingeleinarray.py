import array as arr
a=arr.array('i',[1,5,9,87,65])
n=len(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
for i in range(0,n):
    print(a[i],end=" ")
