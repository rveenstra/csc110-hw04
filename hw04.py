# ------------------------------------------------------
#        Name: (Riley Veenstra)
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys


secret_word = "dog"  # Global variable assigned at top of hw04.py

# Task 1
def check_text():
    """Prompts for a sentence until secret_word or 'dog'/'Dog' is used."""
    global secret_word
    while True:
        sentence = input("Give me a sentence: ")
        
        if secret_word in sentence:
            print("You used the secret word!")
            break
        elif "dog" in sentence or "Dog" in sentence:
            print('You used the word "dog" or the word "Dog"!')
            break
        else:
            print("Try again")


# Task 2
#ask for 2 integers and tell us which is larger
def check_greater():
    """Prompts for two integers until one is greater than the other."""
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
#find all number between 1 and 40 that meet our conditions
def get_special_numbers():
    """Prints numbers between 1 and 40 that are odd, multiples of 3, and not multiples of 5."""
    for num in range(1,41):
        if num % 2 != 0 and num % 3 == 0 and num % 5 != 0:
            print(num)
    
    


# Task 4.a
#Ask for a string and let us know which letters are vowels or consonants
def my_for_loop():
    """Validates string length/spaces and prints vowel/consonant status for each character."""
    str = input("Give me a string: ")
    if len(str) < 2 or len(str) > 5 or " " in str:
        print("bad word")
        return

    vowels = "aeiouAEIOU"

    for char in str:
        if char in vowels:
            print(f"{char} is a vowel")
        else:
            print(f"{char} is a consonant")

# Task 4.b
#give 3 options each with a different output
def my_while_loop():
    """Offers options 'a', 'b', or 'c' to the user until 'b' returns or 'c' exits."""
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
