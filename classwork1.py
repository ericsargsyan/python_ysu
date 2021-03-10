# 1

sum_ = 0
for i in range(1, 101):
	if i == 10:
		continue
	sum_ += 1 / (i ** 2 - 100)	

print(sum_)

# 2
ls = [1, 2, 13, 26, 222, 49, 71, 78]

ls_13 = [i for i in ls if i % 13 == 0]

print("divisible by 13", ls_13)


sum1 = 0
n = 1
while n <= 5:
	sum1 += n
	n += 1
print(sum1)	


sum2 = 0
i = 1
while sum2 < 100000:
	sum2 += i
print(sum2)	


def my_function(num: int) -> int:

	return num**2 - 2 * num + 1

print("result at 0", my_function(0))
print("result at 1",my_function(1))
print("result at 2",my_function(2))	


def sgn(num: int) -> int:
	"""
	sgn fucntion 
	return 1 if number is positive
			0 if number is 0 and
			-1 if number is negative
	"""
	if num > 0:
		return 1
	elif num < 0:
		return -1
	return 0

print(sgn(0))
print(sgn(2))
print(sgn(-2))	
print(sgn.__doc__)

def next_function(num1: int, num2: int) -> int:
	return 3 * num1 ** 2 + 5 * abs(num2)

print(next_function(1, -5))		


def triangle_area(base, height=1) -> int:
	return base * height / 2

print(triangle_area(5))	


def is_prime(number) -> bool:
	for i in range(2, int(number // 2) + 1):
		if number % i == 0:
			return False
	if number == 2:
		return True		
	return True
	
print(is_prime(2))			


def prime(number):
	prime_number = []
	for i in range(2, number + 1):
		if not is_prime(i):
			prime_number.append(i)

	return prime_number
	
print("prime nubmers: ", prime(15))			