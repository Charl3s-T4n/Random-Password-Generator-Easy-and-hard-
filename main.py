#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#To print letters using random.randint() method
easy_password = ""                                      # Want to concatenate onto this empty string
for letter in range(1,nr_letters + 1):
  index_of_letter = random.randint(0,52 - 1)
  letter = letters[index_of_letter]
  easy_password += letter 
# To print symbols
for symbol in range(1,nr_symbols + 1): 
  index_of_symbol = random.randint(0,9 - 1)
  symbol = symbols[index_of_symbol]
  easy_password += symbol
# To print numbers using random.choice() method instead, both methods work
for number in range(1,nr_numbers + 1):
  number = random.choice(numbers)
  easy_password += number 
# Print password
print(f"Your 'EASY' password is: {easy_password}")




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Essentially, using random.shuffle(list)
new_list_of_characters_of_chosen_pw = list(easy_password)    #Make password into a list 
random.shuffle(new_list_of_characters_of_chosen_pw)#Shuffle the characters in the list
hard_password = ''.join(new_list_of_characters_of_chosen_pw)  # Join back the characters into single password
print(f"Your 'HARD' password is: {hard_password}")