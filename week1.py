figure1 = int(input("Please enter a number: "))
figure2 = int(input("\n Please enter another number: "))
operation = input("\n Now enter an operation you want us to perform: ")
answers = [figure1, figure2]

for answer in answers:
    if operation == '+':
        print(figure1 + figure2)
    elif operation == '-':
        print(figure1 - figure2)
    elif operation == '*':
        print(figure1 * figure2)
    elif operation == '/':
        print(figure1 / figure2)
    else:
        break
