#Problem 3: What is the largest prime factor of the number 600851475143 ?
import math
n = 600851475143
num = []

if(n%2==0):
    num.append(2)
    while(n%2==0):
        n /= 2
for i in range (3, int(math.sqrt(n))):
    if(n%i==0):
        num.append(i)
        n /= i
if(n>1):
    num.append(n)
print(max(num))