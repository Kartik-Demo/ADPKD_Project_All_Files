number = 12345
sum_digits = 0
while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10
print("sum of digits:-",sum_digits)