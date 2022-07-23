#1 First task :
"""
You have a range of numbers find a sum of range your numbers.
"""

my_list = []
count = 0

def is_prime(n):
    for i in range(2,n//2+1):
        if n%i == 0 :
            return False
    return True

i = 2
while count <100:
    if is_prime(i):
        my_list.append(i)
        count+=1
    i +=1

print(my_list,len(my_list))
print(sum(my_list))

##############################################

#2 Second task :
"""
Write a function which take as arguments string and count how much string in Upper and lower.
"""
my_string = "Hello, I`m a string and we will Find Out lower & UPPER."


def count_str(my_string):
    symb_lower = 0
    symb_upper = 0
    for let in my_string:
        if let.islower():
            symb_lower+=1
        elif let.isupper():
            symb_upper+=1
    return f"All lower letters are : {symb_lower}. All upper letters are : {symb_upper}"

print(count_str(my_string))

#####################################################

#3 Third task :
"""
Write a function which take as argument a string like 'apple-bannanas-potato' and return this string sorted.
"""

my_string = "Hello-how-are-you-Like-you-."
my_string_2 = "green-red-yellow-black-white"

def sort_words(my_string):
    change_to_list = my_string.split("-")
    change_to_list.sort()
    return "-".join(change_to_list)

print(sort_words(my_string))
print(sort_words(my_string_2))

######################################################

#4 Fourth task :
"""
Write a function which take as arguments a numbers and find out arithmetic midle and return , only those numbers which is low as our 
midle-arithmetic.
"""

def find_midle(*args):
    my_list = []
    midle_numb = sum(args)/len(args)
    print("The midle is :", midle_numb)

    for numb in args:
        if numb <= midle_numb:
            my_list.append(numb)
    return my_list

print(find_midle(1,2,3,4,5,6,7,8,9))
#####################################################

#5 Fifth task :
"""
Write a function which take voluntary numbers and return a reverse list.
Or if user want the programm will return only odd numbers.
"""
def change_numbers(*args,only_odd=False):
    if only_odd is False:
        my_list_numb = []
        for i in args:
            my_list_numb.append(i)
        return my_list_numb[::-1]
    elif only_odd is True:
        my_list_numb = []
        for i in args:
            if i % 2==1:
                my_list_numb.append(i)
        return my_list_numb[::-1]

print(change_numbers(1,2,3,4,5,only_odd=True))
#####################################################

#6 Sixth task :
"""
Write a function which input some information of user and return as a shablon.
"""

def user_information(**kwargs):
    if "name" not in kwargs or "last_name" not in kwargs:
        return ("Please enter your name & Last name.")
    print("Name: ",kwargs["name"],"\n"
          "Last name: ",kwargs["last_name"])

    if len(kwargs) > 2:
        print()
    keys = list(kwargs.keys())[2:]
    keys.sort()
    for inf in keys:
        print(f"{inf}: {kwargs[inf]}")
    print("-"*30)

user_information(name="Jaik",last_name="Koaew")
user_information(name="Mike",last_name="Aber",age=23,email="example@xa.com",phone="981-123-948",)
user_information(name="Kile",last_name="Ofark",age=30,email="example@gmail.com",phone="310-198-152",dog="Djeck")

#####################################################

#7 Seventh task :
"""
You have a list of numbers delete all numbers >0 and find out a sum of this numbers 

Second use a lambda.

"""

my_numbers = [2, 1,-5, 7, -1,13,-9, 5,-24, 18, 4]

def find_and_delete(some_list):
    list_of_negative_numbs = []
    for i in some_list:
        if i < 0:
            list_of_negative_numbs.append(i)
    return list_of_negative_numbs

print(f"With using a function : {sum(find_and_delete(my_numbers))}")

# With lamba:
my_numbers = [1,2,-5,7,-1,4,-9,5, 12,-24,18]

delete_positive_numbers = list(filter(lambda i : i<0 , my_numbers))

print(f"The sum with using lamba : {sum(delete_positive_numbers)}")

#8 Eigth task :
"""
You have a list of names, find out and delete all names which start from small title and find out a length of all names.

"""

list_of_names = ["john","Joe","kile","Roland","mike","Keni"]

def find_and_delete_low(some_list):
    for i in some_list:
        if i[0].isupper() == False:
            some_list.remove(i)
    return some_list

def count_names(list_of_names):
    clear_list = find_and_delete_low(list_of_names)
    length_of_names = 0
    for name in clear_list:
        length_of_names += len(name)
    return length_of_names
        

print(count_names(list_of_names))
# With lambda :

list_of_names = ["john","Joe","kile","Roland","mike","Keni"]

find_and_delete_low_names = list(filter( lambda i: i[0].isupper(),list_of_names))

count_len_names = len(''.join(find_and_delete_low_names))

print(count_len_names)

#9 ninth task :
"""
Create a func which will take a list of numbers , that every element of list will multiplied by his index and multiplied by 3 and than by thus number.
With lambda.

"""
my_numbers_list = [3,5,9]

def multiplied_numbers(some_list):
    result_list = []
    for i in some_list:
        result = i * some_list.index(i)**3
        result_list.append(result)
    return result_list

print(multiplied_numbers(my_numbers_list))

# With lambda :

multiplied_lambda = list(map(lambda i: i*my_numbers_list.index(i)**3, my_numbers_list))
print(multiplied_lambda)

#10 tenth task :
"""
Write a func which count a some example:

n = 6

result = n + (n - 2) + (n - 4) + (n -6)

"""
number = 10

def find_sum(number):
    result = number
    for i in range(2,number,2):
        result +=  number-i
    return result

print(find_sum(number))

#11 eleventh task :
"""
Write a function which find out a sum of list , even if list have another list.

"""
lst_of_numbers = [1,2,[3,4],5,6]

def count_sum(some_lsit):
    sum_of_all_numbers = 0
    for numbers in some_lsit:
        if type(numbers) is list:
            sum_of_all_numbers += count_sum(numbers)
        else:
            sum_of_all_numbers += numbers
    return sum_of_all_numbers
            
print(count_sum(lst_of_numbers))
