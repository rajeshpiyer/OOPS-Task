class square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side

print("\n-- Area & Perimeter of Square --")
side = int(input("Enter the side of square (cm): "))
s1 = square(side)
area = s1.area()
perimeter = s1.perimeter()

print(f"Square 1 : \nArea : {area} sqcm\nPerimeter : {perimeter} cm")
