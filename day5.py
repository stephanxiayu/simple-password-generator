#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers= int(input(f"How many symbols would you like?\n"))
nr_symbols = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# pick a random choice from a list of strings.
password = random.choice(letters)
passNumbers=random.choice(numbers)
passSym=random.choice(symbols)
# Output 'The Shawshank Redemption'
list=[]

for i in range(nr_letters):
    password = random.choice(letters)
    list.append(str(password))
# print(f"mein password ist {list}")
for i in range(nr_symbols):
    passSym=random.choice(symbols)
    list.append(str(passSym))

for i in range(nr_numbers):
    passNumbers=random.choice(passNumbers)
    list.append(str(passNumbers))


newList=[]
for e in range(nr_letters+nr_symbols+nr_numbers):
    new=random.choice(list)
    newList.append(str(new))




print(f"dein neus passwordt ist {''.join(newList)}")
# Output 
# 'Citizen Kane'
# 'The Shawshank Redemption'





      











    

   


  
    


     