number=int(input("enter a number :"))
factors=[]
for i in range(1,number+1):
	if number%i == 0:
		factors.append(i)
print(f"factors of {number} are : {factors}")
