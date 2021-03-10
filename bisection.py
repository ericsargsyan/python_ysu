# Bisection Algorithm

f = lambda x: x ** 2 - 2


def bisection_algorithm(a: int, b: int) -> float:
	if f(a) * f(b) >= 0:
		return "Bolzano–Cauchy Theorem doesn't work in this case"
	
	for i in range(100):
		c = (a + b) / 2

		if f(a) * f(c) < 0:
			b = c
		elif f(a) * f(c) > 0:
			a = c
		else:
			return "Bolzano–Cauchy Theorem doesn't work in this case"
			
	return c

print(bisection_algorithm(-1, 2))
