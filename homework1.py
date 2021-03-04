#Calculate the values of the Expression

x = pow(2, 10) + pow(3, 10)
y = pow(x, 0.5)

print(y)

#define a list

ls = [1, 1, 2, 3, 2, 3, 1, 1, 2, 3, 4, 1]
print(ls)

#get the length of the list in variable 'l'

l = len(ls)
print(l)

#Change the last element of the list by 5

ls[l-1] = 5
print(ls)

#Extract all odd-indexed elements of the list in the list y, and all 
#even-indexed elements of list into the list z

y = [ls[i] for i in range(len(ls)) if i % 2 == 0]

z = [ls[i] for i in range(len(ls)) if i % 2 != 0]

print("odd_list: ", y)
print("even_list: ", x)

#Get all even elements of x in the list y1 and all odd elements of $x$ in the list z1

y1 = [ls[i] for i in range(len(ls)) if ls[i] % 2 == 0]

z1 = [ls[i] for i in range(len(ls)) if ls[i] % 2 != 0]

print("even_el_list: ", y1)
print("odd_el_list: ", z1)
#Find the sum of the elements of the list

sum_ = 0
for i in ls:
	sum_ = sum_ + ls[i]
print(sum_)

#Construct a list I consisting of all reciprocals of the elements of the list

I = [1/ls[i] for i in ls]
print("reciprocals list: ", I)

#Find the value of the sum

k = [1/pow(3,k) for k in range(1, 11)]

print(sum(k))

#Find the number of letters in this word

text = 'Pneumonoultramicroscopicsilicovolcanoconiosis'

print(len(text))

#Find the number of letters "o" in this word

count_ = text.count('o')
print(count_)

#Find the number of vowels (ձայնավորներ) in this word

v = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

vowels = [i for i in text if i in v]

print(len(vowels))
