a = eval(input("enter the number between 0 -999 :"))
total = 0
while(a>0):
	dig = a%10
	total = dig + total
	a = a//10
print("the sum of the digits is",total)
