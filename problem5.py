#Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#f(n)=∏ipqii=pq11×pq22×⋯
def powercheck(n, total):
    pow = 1
    check = n
    if(total/n > 1):
        while((n**(pow+1)) <= total):
            pow += 1
            check = n**pow
    print(str(n)+"^"+str(pow))
    return pow

#all primes <= 20
primes = [2,3,5,7,11,13,17,19]
ans = 1
for i in primes:
    ans *= i**powercheck(i, 20)
print("\n" + str(ans))
