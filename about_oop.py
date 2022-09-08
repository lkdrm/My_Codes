# from about_os import Car

from square import Square,RegularSqrPrisma,Triangle,EquilateralTriangle

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

the_triangle = [Triangle(2,5,6), Triangle(5,2,4), Triangle(7,3,6)]
the_equal_triangle = [EquilateralTriangle(5), EquilateralTriangle(8), EquilateralTriangle(6),EquilateralTriangle(4)]

# print(the_triangle[0].print_triangle())
# print(the_equal_triangle[0].exists())
# the_triangle[0].get_angles()
# the_triangle[0].get_perimetr()
# the_triangle[0].get_square()

triangle_s = list(map(lambda triangle : triangle.get_square(), the_triangle))
triangle_s_avg = sum(triangle_s) / len(triangle_s)

equila_triangle_maximum_p = max(the_equal_triangle, key = lambda triangle: triangle.get_perimetr())

print("*"*50)
print(f"The average triangles square: {triangle_s_avg:.2f}")
print(f"The equilateral triangle with the max perimeter is : {equila_triangle_maximum_p.print_triangle()}")