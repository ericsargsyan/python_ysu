import random

# Problem 1 Dictionaries

cities_AM = {"Yerevan": 1077600, "Hrazdan": 40400, "Vanadzor": 79300, "Gyumri": 114500, "Kapan": 57000}

for i in cities_AM:
	print(i)

population = 0

for i in cities_AM.values():
	population += i

print("Population: ", population)	 	

def sort_descending_v(dictionary: dict):
    # dictionary = sorted(dictionary.keys())
    ls = list(dictionary.items())
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][1] > ls[j][1]:
                ls[i], ls[j] = ls[j], ls[i]
    dictionary = dict(ls)
    return dictionary

second_largest = list(sort_descending_v(cities_AM).items())[1]

print(f"Second largest city in Armenia is {second_largest[0]} which population is {second_largest[1]:,}")    


# Adding 6th city
cities_AM.update({"Ijevan": 20500})
print(cities_AM)


# adding areas
areas = [223, 152, 32, 54, 36, 4.6]

keys = [key for key in cities_AM]

cities_AM.update({keys[i]: (cities_AM[keys[i]], areas[i]) for i in range(len(cities_AM))})
print(cities_AM)

cities_GE = {"Berlin": 3769495, "Hamburg": 1845229}


countries = {
	"Armenia": cities_AM,
	"Germany": cities_GE				
}

print(countries)

# Problem 2 Control flows

x = [1, -2, 3, 9, 0, 1, 3, 2, -2, -4, 1, -3]

x_pos = [i for i in x if i > 0]
x_neg = [i for i in x if i < 0]

print("Positive lists: ", x_pos)
print("Negative lists: ", x_neg)


ind_pos = [i for i in range(len(x)) if x[i] > 0]
ind_neg = [i for i in range(len(x)) if x[i] < 0]


print("Positive indexes: ", ind_pos)
print("Negative indexes: ", ind_neg)


# sum of 1 + 3 + 5 + ... + 101

sum_ = 0

for i in range(1, 102, 2):
	sum_ += i

print("1 + 3 + 5 + ... + 101 = ", sum_)

# 1 + 1/2 + 3 + 1/4 + ... + 99 + 1/100

sum__ = 0

for i in range(1, 101):
	if i % 2 != 0:
		sum__ += i
	else:
		sum__ += 1 / i

print("1 + 1/2 + 3 + 1/4 + ... + 99 + 1/100 = ", sum__)


# 20!!

semifactorial = 1

for i in range(2, 21, 2):
	semifactorial *= i

print("20!! = ", semifactorial)


# Sum of (-1)^k / k! k changes from 0 to 20

def my_facatorial(number: int) -> int:
	factorial = 1
	for i in range(2, number + 1):
		factorial *= i
	return factorial

_sum = 0

for i in range(0, 21):
	_sum += ((-1) ** i) / my_facatorial(i)

print("(-1)^k / k! = ", _sum, "where 0 <= k <= 20")


# |S_n - 2 <= 0.001|

s_n = 0
n = 1
while True:
	
	for i in range(n + 1):
		s_n += i / 2 ** i

	if abs(s_n - 2) <= 0.001:
		print(f"Min n satisfing |S_n - 2 <= 0.001| is {n}")
		break
	s_n = 0	
	n += 1	

# maximum element

def max_(random_list: list) -> float:
	max_element = random_list[0]

	for i in random_list:
		if max_element < i:
			max_element = i
	return max_element
			
random_list = [round(random.uniform(-100, 100), 2) for i in range(22)]

print(random_list)

print(f"Maximum element in the above list  is {max_(random_list)}")		


# Sort list in increasing order

def bubble_sort(arr: list) -> list:
    for i in range(len(random_list)):
        for j in range(len(random_list) - 1):
            if random_list[j] > random_list[j + 1]:
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
    return random_list


def insertion_sort(random_list: list) -> list:
    for i in range(len(random_list)):
        while i > 0 and random_list[i - 1] > random_list[i]:
            random_list[i], random_list[i - 1] = random_list[i - 1], random_list[i]
            i -= 1
    return random_list

print(bubble_sort(random_list))
print(insertion_sort(random_list))


# Problem 3 Functions

def function1(x):
	if x < 0:
		return -1
	elif x in range(0, 6):
		return 4
	return 9
	
ls1 = [-4, 3, 7]
value_list1 = [function1(i) for i in ls1]

print(f"Function values at the points {ls1}\n{value_list1}")	

def function2(x):
	if x in range(0, 11):
		return 	0
	return 1
	
ls2 = [-4, 0, 17]
value_list2 = [function2(i) for i in ls2]	
print(f"Function values at the points {ls2}\n{value_list2}")


# Fibonacci Series

def fibonacci(n: int):
	print(f"Fibonacci Series up to the {n}")
	f1 = 0
	f2 = 1
	while f1 <= n:
		print(f1, end=' ')
		f3 = f1 + f2
		f1 = f2
		f2 = f3	

# validating number
n = int(input("Input nubmer: "))			
while True:
	if n > 0:
		break
	else:
		print("Number must be posotive!")
	n = int(input("Input nubmer: "))

fibonacci(n)

def binomial_coefficients(n: int):
	for k in range(0, n + 1):
		print(int(my_facatorial(n) / (my_facatorial(n-k) * my_facatorial(k))), end=' ')


number = int(input("Input number: "))

binomial_coefficients(number)

# Addition Binomial Triangle

print("Pascal's Triangle")
for i in range(number):
	binomial_coefficients(i)
	print("\n")
