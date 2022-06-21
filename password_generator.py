import random

print("This program will create a password from jour words.",
      "First of all you need to write some text and then a len of your password.",
      "But len of your pass must be min 8 symbols.",sep="\n")

def password_generator():
    count = 0
    new_password = []
    while True:
        try:
            words = input("Enter here your text : ")
            len_of_pass = int(input("Enter here the len of your pass : "))
            if len(words) >= 8:
                False
                while count != len_of_pass:
                    choice_rand_word = random.choice(words)
                    choice_rand_letter = random.choice(choice_rand_word)
                    if choice_rand_letter == " ":
                        pass
                    else:
                        new_password.append(choice_rand_letter)
                        count +=1
                pass_prt = "".join(new_password)
                return f"Your password is : {pass_prt}"
            else:
                print("Your text must to be min 8 symbols.")
        except ValueError:
            print("Please enter a correct values.")

def to_txt():
    with open("New_password.txt","w") as file:
        file.write(password_generator())
        print("Your password has been created.")

to_txt()
