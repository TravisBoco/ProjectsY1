# Grabs random inputs
import random
# Grabs lowercase and Uppercase Letters and special characters
import string

# Function to generate the password then has parameters (things needed to call the function) This also goes in order of what would be passed through
def generate_password(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters # Grabs all potential letters
    digits = string.digits #Grabs all potential digits
    special = string.punctuation # Grabs all special char

    # if variable is ture it will take digits add into letter string and if special chars we add to characters which we can select from when genning password
    # create a string from all dif char we could be selecting from
    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    # variables pwd stores the password and meets_criteria is false but when it has lenght required and digits and special chracters it will turn true and etc
    pwd = "" # password is empty
    meets_critera = False # does not meet criteria
    has_number = False
    has_special = False

    # while it does not meet the criteria or lenght is less than min lenght
    while not meets_critera or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # if new chracvter in digit then has number is true and new char in special then change to ture
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # if we include number meets criteria will be true  and if we have special char meets critiera will have meet criteria and will have special if has number but dont include it
        # if we had a number meets criteria is true and if we have speciual its true but no number but special meets criterias is false
        meets_critera = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special
    
    return pwd


# outputs
#we ask min lenght has to be an int
#ask if they want number then cast to lowercase and it has to be a y  and if true will include a number
#the generates a password
    
min_length = int(input("Enter min length"))
has_number = input("Would you like to have numbers (y/n)? ").lower() == 'y'
has_special = input("Would you like to have special chracters (y/n)? ").lower() == 'y'
pwd = generate_password(min_length, has_number, has_special)
print("Your generated password is", pwd)