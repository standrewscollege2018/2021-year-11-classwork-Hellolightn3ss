
y= 2
z= 0
num=1
while num < 4000000:
    num = num + y
    if num % 2 ==0:
        z = z + num
    y = y + num
    if y % 2 ==0:
        z = z + y
print (z)