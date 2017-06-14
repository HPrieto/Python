print("Hellok")

#print integer and float
print("5/3: ")
print(5/3)
print(5//3)

#integer input and output
radius = float(input("Radius: "))
print("The area is: ",3.14*radius**2)

x = 5
y = 6

print("X = 5")
print("Y = 6")
if x > y:
	print("X is greater than y.")
elif x < y:
	print("X is less than y.")
else:
	print("X is equal to y.")

#While loop
product = 1
value   = 1
while value <= 10:
	product*=value
	value+=1
print(product)

#For loop
product = 1
for value in range(1,11):
	product*=value
print(product)

print("Heriberto"[3])
print("Heriberto"[-3])

print("greater[:]")
print("greater"[:])

print("greater[2:]")
print("greater"[2:])

print("greater[:2]")
print("greater"[:2])

print("greater[2:5]")
print("greater"[2:5])

print("heriberto[4:]")
print("heriberto"[:4])

#String Right or Left Justification
print("%6s"%"four")
print("%-6s"%"four")

#format Digit Justification
for exponent in range(1,6):
	print("%-3d%12d"%(exponent,10**exponent))

for nExponent in range(6,11):
	print("%-3d%12d"%(nExponent,10**nExponent))

salary = 10000000.0
print("Your salary at Jogar is: $"+str(salary))
print("Your salary at Jogar is: $%0.5f"%salary)

#Format string/Occupy width
print("%10.5f"%3.123541352345)

#Objects and method calls
print("'heriberto'.isupper()")
print("heriberto".isupper())

print("'heriberto.upper()'")
print("heriberto".upper())

print("'heriberto'.startswith('heri')")
print("heriberto".startswith("heri"))

#Options when working with strings
print("Length of Heriberto")
print(len('heriberto'))
print('heriberto'.__len__())

print('Concat Heri + berto')
print('Heri'+'herto')
print('Heri'.__add__('berto'))

print('Check if string contains value:')
print('heri' in 'heriberto')
print('heriberto'.__contains__('heri'))