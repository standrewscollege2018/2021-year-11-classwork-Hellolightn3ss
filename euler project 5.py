
y=0
factors=[]
for num in range (1,20):
        for i in range(2,num-1):
            if (num % i) == 0:
                y=y+1
            else:
                factors.append(num)

print(factors)







