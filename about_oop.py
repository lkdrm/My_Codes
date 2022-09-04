# from about_os import Car
from square import Square,RegularSqrPrisma

# first_car = Car(2015,"Mercedes-benz","GLC")

# print(first_car)
# print(first_car.start_engeen())
# print(first_car.stop_engeen())


the_square = [Square(4),Square(8),Square(5),Square(3)]
the_prisms = [RegularSqrPrisma(3,5), RegularSqrPrisma(2,8),RegularSqrPrisma(9,4)]

max_diag_square = max(the_square,key=lambda squar: squar.calc_diag())
min_prisma = min(the_prisms,key=lambda prsm: prsm.calc_volume())

print("*"*50)
print(f"The square with max is : {max_diag_square.print_info()}")

print("*"*50)
print(f"The min of prisma is : {min_prisma.print_prisma()}")