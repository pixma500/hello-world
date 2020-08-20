#Найдите сумму всех чисел, которые можно записать как сумму пятых степеней их цифр.
x=0
for i in range(2,350000):
	k=0
	for d in str(i):
		k+=int(d)**5
	if i==k:
		x+=i
print(x)

#одна строка
print (sum([n for n in range(2,350000) if sum(int(i)**5 for i in str(n)) == n]))
