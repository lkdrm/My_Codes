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

def user_information(name,last_name,age, some_information):
    return (f"Name:{name}\nLast Name: {last_name}\n\nAge:{age}\n{some_information}\n{'-'*30}")

print(user_information("Jake","Korel",25,"love dogs"))