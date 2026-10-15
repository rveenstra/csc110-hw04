# ------------------------------------------------------
#        Name: (Riley Veenstra)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "Dog" or "dog"

# Task 1
def check_text():
    """ Add your docstring """
    while True:
        sentence = input("Give me a sentence: ")
        if "dog" in sentence or "Dog" in sentence:
            print('You used the word "dog" or the word "Dog"!')
            break
        else:
            print("Try again")




# Task 2
def check_greater():
    """ Add your docstring """
    while True:
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))
        if first == second:
            print("Try again")
        elif first <= second:
            print("Second is Greater")
            break
        else:
            print("First is Greater")
            break
    print("done")
    
        



# Task 3
def get_special_numbers():
    """ Add your docstring """
    for num in range(1,41):
        if num % 2 != 0 and num % 3 == 0 and num % 5 != 0:
            print(num)
    
    


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    str = input("Give me a string: ")
    if len(str) < 2 or len(str) > 5 or " " in str:
        return

    vowels = "aeiouAEIOU"

    for char in str:
        if char in vowels:
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    while True:
        select = input("Choose one option: a, b, or c: ")
        if select == "a":
            pass
        elif select == "b":
            print("Goodbye")
            return
        elif select == "c":
            sys.exit()
        else:
            print("try again")
    
        
    

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
