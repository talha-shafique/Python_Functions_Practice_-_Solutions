def area_of_circle(r):
    area=3.14159*r
    return area
a=int(input("Enter radius of desired circle: "))
print('Area of the circle with radius',a, "is", area_of_circle(a))