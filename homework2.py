import random

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
