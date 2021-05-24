#Problem 2: Considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

ans = 0

fib1 = 0
fib2 = 1
sum = 0

while (sum < 4000000):
    sum = fib1 + fib2
    if (sum%2 == 0):
        ans += sum
    fib1 = fib2
    fib2 = sum

print(ans)
