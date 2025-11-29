class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def __lt__(self, other):
        return self.area()<other.area()

l=int(input("enter length of first rect:"))
b=int(input("enter breadth of first rect:"))
r1=rectangle(l,b)

l=int(input("enter length of second rect:",))
b=int(input("enter breadth of second rect:"))
r2=rectangle(l,b)


if r1<r2:
    print("rectangle 1 is smaller")
else:
    print("rectangle 2 is smaller")
