n = 8395
numbers = []

while n > 0:
    numb = n % 10
    numbers.append(numb)
    n = n // 10
print(numbers)
print(max(numbers))