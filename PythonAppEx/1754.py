
num = input()
fac = 1

for i in range(int(num), 1,-1):
    fac = fac* i

print(fac)


'''
a = input()
print(a)
b = input()
print(b)
##if(len(a) < len(b)):
c = [b, a]
##elif(len(b) < len(a)):
 ##   c = [a,b]

print(c)

c = printBignum(input1, input2)

print(c)

def printBignum(a, b):
    if(len(a) < len(b)):
        return [b,a]
    elif(len(b) < len(a)):
        return [a,b]
    else:
        for i in range(len(a)):
            if(a[i] > b[i]):
                return [a,b]
            elif(b[i] > a[i]):
                return [b,a]




count = 0
sum = 0
for number in range(1, 5000):
    if(number % 17 == 0):
        count += 1
        sum += number

print("개수", count, "합 ", sum)
'''