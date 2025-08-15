import random
import string
import json
import math

def generatePassword(complexity, n): # where n is password length
    match complexity:
        case 1: #Only letters
            a = string.ascii_letters1
        case 2: #letters and numbers
            a = string.ascii_letters + string.digits 
        case 3: #All available characters
            a = string.ascii_letters + string.digits + string.punctuation
        case _:
            return "ERROR: Invalid selection"
    while True:
        try:
            assert 4 < n < 100
        except ValueError:
            print("ERROR: Not a number. Please insert any number from 5 to 99")
            n = int(input("Enter any number from 5 to 99: "))
        except AssertionError:
            print("ERROR: Not a valid number. Please insert any number from 5 to 99")
            n = int(input("Enter any number from 5 to 99: "))
        else:
            break
    pw = "".join(random.sample(a, n))
    return pw

def load_words():
    with open('english-words/words_dictionary.json') as word_file:
            #numbers = [string.digits for number in string.digits]
        valid_words = json.load(word_file)
            #valid_words = [word.strip() for word in word_file] + numbers
        return valid_words

def generatePassphrase(contains_numbers, n): # n = passphrase length
    while True:
        try:
            assert 2 < n < 100
        except ValueError:
            print("ERROR: Not a number. Please insert any number from 2 to 99")
            n = int(input("Enter any number from 5 to 99: "))
        except AssertionError:
            print("ERROR: Not a valid number. Please insert any number from 2 to 99")
            n = int(input("Enter any number from 5 to 99: "))
        else:
            break
    words = load_words()
    if (contains_numbers == False): 
        ps = " ".join(random.sample(list(words), n))
    else:  
        number = [int(x) for x in string.digits]
        ps = " ".join(random.sample((list(words) + number), n)) #such a convoluted way to do this
        #the problem with this approach is that it will not always display a number
        #should I make it so it always displays a number?
    return ps

def calculate_entropy(password):
    password_dissected = list(password)
    password_length = len(password_dissected)
    #E = log2(RL) 
    #R = size of pool of unique characters
    #L = password length
    #initialize the lists I will compare the password with:
    lowercase = list(string.ascii_lowercase) 
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)
    pool = 0
    #setting pool value depending on characters included in the password
    if [character for character in password if character in lowercase]:
        pool =+ 26
    if [character for character in password if character in uppercase]:
        pool =+ 26
    if [character for character in password if character in digits]:
        pool =+ 10   
    if [character for character in password if character in special_characters]:
        pool =+ 32
    entropy = password_length * math.log(pool, 2)  
    return entropy

def statistics(password): # Takes already generated password, calculates statistics such as entropy
    entropy = calculate_entropy(password)
    print("La contraseña tiene una entropía de " + str(entropy) + " bits.")
    #more to come

def main_menu():
    print("Generate password.")
    while True:
        print("Select any option:")
        print("1. Generate password (Default)")
        print("2. Generate passphrase")
        userAction = input("Type any of the numbers above to proceed or press Enter: ")
        if (userAction == "1" or userAction == ""):
            password = menu_password()
            break
        elif (userAction == "2"):
            password = menu_passphrase()
            break
        else:
            print("ERROR: Invalid selection.")
    print(password)
    statistics(password)

def menu_password():
    while True:
        print("Select complexity level of password:")
        print("1. Only letters. This includes uppercase and lowercase letters.")
        print("2. Letters and numbers.")
        print("3. Letters, numbers and special characters (Default).")
        choice = input("Input your selection, or press Enter to continue: ")
        if (choice == "3" or choice == ""):
            complexity = 3
            break
        elif (choice == "1"):
            complexity = 1
            break
        elif (choice == "2"):
            complexity = 2
            break
        else:
            print("ERROR: Invalid selection.")
    n = int(input("Select password length (Cannot be less than 5, maximum 99): "))
    return generatePassword(complexity, n)

def menu_passphrase():
    while True:
        choice = str(input("Should the passphrase contain numbers? (Y/n): ")).lower()
        match choice:
            case "y":
                has_numbers = True
                break
            case "n":
                has_numbers = False
                break
            case "":
                has_numbers = True
                break
            case _:
                print("ERROR: Invalid selection.")
    n = int(input("Select passphrase length (Cannot be less than 2, maximum 99): "))
    return generatePassphrase(has_numbers, n)

def main():
   return main_menu()


if __name__== "__main__":
    main()