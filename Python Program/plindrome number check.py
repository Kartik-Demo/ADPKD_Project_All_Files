import math
def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))
test_number =int(input("\n Enter Your Number:-"))
print ("\n The original number is :- " + str(test_number))
res = test_number == rev(test_number)
print ("\n Is the number palindrome ? :- " + str(res))
