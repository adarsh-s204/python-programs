from graphics.rectangle import area as rect_area,perimeter as rect_perimeter
from graphics.circle import area as circle_area,perimeter as circle_perimeter

from graphics.3D_graphics.cuboid import surface_area as cuboid_surface_area,volume as cuboid_volume

from graphics.3D_graphics.sphere import surface_area as sphere_surface_area,volume as sphere_volume

print("enter the length and breadth of the rectangle :")
l=int(input("length :"))
b=int(input("breadth :"))
print("rectangle area :",rect_area(l,b))
print("rectangle perimeter :",rect_perimeter(l,b))
print("\n\n")
print("enter the radius of the circle :")
radius=int(input("radius :"))
print("circle area :",circle_area(radius))
print("circle perimeter :",circle_perimeter(radius))
print("\n\n")
print("enter the dimension of the cuboid :")
length =float(input("length :"))
width =float(input("width :"))
heigth =float(input("height :"))
print("cuboid surface area :",cuboid_surface_area(length,width,height))
print("cuboid volume :",cuboid_volume(length,width,height))
print("\n\n")
print("enter the radius of the sphere : ")
radius =float(input("radius :"))
print("sphere surface area :",sphere_surface_area(radius))
print("sphere volume :",sphere_volume(radius))
