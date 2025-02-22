from array import array as arr
a=arr('i',[1,25,225])
print(a)
a. append(5)
print(a)
print(a.buffer_info, 'memory address')
a.byteswap()
print(a)
print(a.count(1))
