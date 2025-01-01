#To welcome the user to this python quiz game
print( "HELLO ALL! Welcome to this fun quiz game about Python! ")

#Asking whether the user the wants to play the game
ans=input("Do you want to play? ")

#Checking if the reply of the user is YES or not
if ans.lower() != "yes":
    quit()

#Asking the user's name
name=input("Enter your name: ")
score=0

#Asking the first question to the user
answer=input("01. Who found Python programming language? ")
if answer.title() == "Guido Van Rossum":  # str.title() method makes the first letter of each word capital
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#Asking the second question to the user
answer=input("02. What is the output of the following Python code?\n x = 5\n y = 2\n print(x ** y)\n ")
if answer == "25":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#Asking the third question to the user
answer=input("03. What is the data type of the following variable in Python?\n my_variable = 'Hello, World!'\n ")
if answer.capitalize() == "String": #str.capitalize() method makes only* the first letter of that word or phrase capital, the rest are lowercase 
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#Asking the fourth question to the user
answer=input("04. What will be the output of the following Python code?\n my_list = [10, 20, 30, 40, 50]\n print(my_list[2]) ")
if answer == "30":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#Asking the fifth question to the user
answer=input("05. What is the output of the following code?\n try:\n\t x = 1 / 0\n except ZeroDivisionError:\n\t print('Error: Division by zero.')\n a) Error: Division by zero.\n b) None\n c) SyntaxError\n d) ZeroDivisionError\n")
if answer.lower() == "a":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#Asking the sixth question to the user
answer=input("06. What will be the output of the following code?\n dog1 ='Buddy'\n print(dog1.upper())\n")
if answer == "BUDDY":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("\n")

#To print the score and appreciate the user
print(f"You have scored {score}/6!")

if score >= 4:
    print(f"********************Congratulations {name}!*****************")
else:
    print(f"*******************Good try, {name}.*********************Keep Trying.******************")
          
