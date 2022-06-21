while True:
    list_of_unique_numbs = []
    print()
    print("Enter a sequence of numbers from and to")
    print("If number 1 and number 2 == 0.",
          "Progamm will exit", sep="\n")
    number_1 = input("Enter first number: ")
    number_2 = input("Enter second number: ")
    try:
        if number_1 == number_2:
            break
        for i in range(int(number_1),int(number_2)):
            if len(str(i)) == 1 :
                list_of_unique_numbs.append(i)
            elif len(str(i)) == 2 :
                numb = str(i)
                if numb[0] != numb[-1]:
                    list_of_unique_numbs.append(numb)
            elif len(str(i)) == 3 :
                numb = str(i)
                if numb[0] != numb[1] and numb[0] != numb[-1] and numb[1] != numb[-1]:
                    list_of_unique_numbs.append(numb)
        print()
        print(f"The list of all unique numbers : {list_of_unique_numbs}.\nAll unique numbers are : {len(list_of_unique_numbs)}" )
    except:
        print("Write only a numbers.")
        print("Work only to 999 numbers.")
