x =0
y =0
for num in range (1,775146):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                y=y+1
            else:
                if num > x:
                    x = num

print(x)





