import random
import os
from password_ascii_art import password_art

def clear_screen():
                if os.name == 'nt':
                    os.system('cls')

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
characters = ["!","@","#","$","&","*"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]


def password_generaor():
    print(password_art)
    user_letter = int(input("enter the number of letters you want in your password: "))
    user_char = int(input("enter the number of characters you want in your password: "))
    user_num = int(input("enter the number of numbers you want in your password: "))

    password_list = []

    for letter in range(0, user_letter):
        password_list += random.choice(letters)

    for character in range(0, user_char):
        password_list += random.choice(characters)

    for number in range(0, user_num):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"your password is {password}")

while True:
    clear_screen()
    password_generaor()
    restart = input("do you want to restart the program (y/n): ")
    if restart == "n":
        clear_screen()
