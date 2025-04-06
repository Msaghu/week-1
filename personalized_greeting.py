## Create a program that asks for the user’s name and favorite color, 
# then prints a personalized greeting like: “Hello, [Name]! Your favorite color, [Color], is awesome!”

user_name = input("Welcome!Please enter your name: ").title()
favourite_colour = input("Thank you. Now enter your favourite colour: ")

greeting = f"Hello, {user_name}! Your favorite color, {favourite_colour}, is awesome!"
print(greeting)