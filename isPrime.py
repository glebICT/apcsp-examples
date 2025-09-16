numbers = [4, 6, 8, 9, 11, 13, 15, 16, 17, 19]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for value in numbers:
    if isPrime(value):
        count += 1
    count += 1
print(count)

