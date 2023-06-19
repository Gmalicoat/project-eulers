tlist = []
num1 = 0
num2 = 1
total = 0
while(total <= 4000000):
    total = num1 + num2
    num1 = num2
    num2 = total
    if(total % 2 == 0):
        tlist.append(total)
print(sum(tlist))
