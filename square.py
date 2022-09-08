from math import sqrt, degrees, acos

class Square:
    def __init__(self,side:int):
        self.side = side
    
    def calc_diag(self):
        d = round(self.side * sqrt(2),2)
        print(f"Diagonal is : {d}")
        return d
    
    def calc_perim(self):
        p = 4 * self.side
        print(f"Perim is {p}")
        return p
    
    def calc_square(self):
        s = self.side ** 2
        print(f"The square is {s}")
        return s
    
    def print_info(self):
        return f"Square: side -- {self.side}"


class RegularSqrPrisma(Square):
    def __init__(self, side: int, height:int):
        super().__init__(side)
        self.height = height
    
    def calc_volume(self):
        v = super().calc_square() * self.height
        print(f"The volume is: {v}")
        return v

    def print_prisma(self):
        return f"Regular square prisma is : base side -- {self.side} & height is -- {self.height}"

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def print_triangle(self):
        return f"ABC (A-{self.a}, B-{self.b}, C-{self.c})"
    
    def exists(self):
        if(self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return f"{self.print_triangle()} - is exist"
        else:
            return f"{self.print_triangle()} - doesn`t exist"
    
    def print_sides(self):
        return f"Sides : {self.a}, {self.b}, {self.c}"
    
    def get_angles(self):
        cos_CAB = acos((self.a**2 + self.c**2 - self.b**2)/(2*self.a * self.c))
        cos_ABC = acos((self.a**2 + self.b**2 - self.c**2)/(2*self.a * self.b))
        cos_BCA = acos((self.b**2 + self.c**2 - self.a**2)/(2*self.b * self.c))

        print(f"CAB: {cos_CAB:.2f} Rad, {degrees(cos_CAB):.2f} Grad")
        print(f"ABC: {cos_ABC:.2f} Rad, {degrees(cos_ABC):.2f} Grad")
        print(f"BCA: {cos_BCA:.2f} Rad, {degrees(cos_BCA):.2f} Grad")
    
    def get_perimetr(self):
        p = self.a + self.b + self.c
        print(f"Perimetr is: {p}.")
        return p

    def get_square(self):
        p = (self.a + self.b + self.c)/2
        s = sqrt(p * ((p-self.a) * (p-self.b) * (p-self.c)))
        print(f"The square is: {s:.2f}")
        return s

class EquilateralTriangle(Triangle):
    def __init__(self, a,):
        super().__init__(a,a,a)

#inheritance