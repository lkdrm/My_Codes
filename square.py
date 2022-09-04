from math import sqrt

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