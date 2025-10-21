result=[]
start=int(input("enter the starting range (4-digit no):"))
end=int(input("enter the ending range (4-digit no):"))
if start<1000 or end>9999 or start>end :
    print("invalid range.please enter valid  4-digit range :")
else:
    for num in range(start,end+1):
        if num%2==0:
            root=int(num**0.5)
            if root*root==num:
                result.append(num)
print("4-digit even perfect square numbers in the given range :")
print(result)
