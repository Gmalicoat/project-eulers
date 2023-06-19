numlist = []
for number in range(1000):
    if(number % 3 == 0 or number % 5 == 0):
        numlist.append(number)
print(sum(numlist))
