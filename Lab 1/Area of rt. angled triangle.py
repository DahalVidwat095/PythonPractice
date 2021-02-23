''''Write a program that reads the length of the base and the height of a right angled triangle and
prints the area .Every number is given on a separate line'''
Base=int(input("enter the base:"))
Height=int(input("enter the height:"))
area=(Base*Height)//2
# the floor division // rounds the result down to the nearest whole number

print(f"The area of the given triangle is {area} sq. cm")