#Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
squaredSum = 0
sumSquares = 0
for i in range(1, 101):
    sumSquares += (i ** 2)
for i in range(1, 101):
    squaredSum += i
squaredSum = squaredSum ** 2

ans = squaredSum - sumSquares
print(ans)