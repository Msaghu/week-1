goodjokes = input("Are you ready for a funny joke session?:")
jokes = {
    "How do trees get on the Internet?": "They log in.", 
    "What do computers like to eat?" : "Chips.",
    "What do you call a space magician?": "A flying saucerer.", 
    "What is a computer’s first sign of old age?": "Loss of memory.",
    "What does a baby computer call his father?": "Instead of Da-da it says “Da-ta.”",
    "What is an astronaut’s favorite control on the computer keyboard?" : "The space bar.",
    "What happened when the computer fell on the floor?": "It slipped a disk.",
}

import random
x=0
D=0
for i in range(7):
    key = random.choice(list(jokes))
    print(key,'?')
    useranswer=input('')
    if useranswer=='quit':
        print('You have chosen to quit')
        break
    elif not useranswer.isalpha():
        print('Numbers not allowed')
        useranswer = input('')
        if useranswer == jokes[key].lower() or useranswer == jokes[key]:
            print(jokes[key],'is correct')
            x=x+1
            del jokes[key]
            
        elif useranswer != jokes[key]:
            print(useranswer,'is not correct')
            print('The correct answer is', jokes[key])
            D=D+1
            del jokes[key]
            

    elif useranswer == jokes[key].lower() or useranswer == jokes[key]:
        print(jokes[key],'is correct')
        x=x+1
        del jokes[key]
    elif useranswer != jokes[key]:
        print(useranswer,'is not correct')
        print('The correct answer is', jokes[key])
        D=D+1
        del jokes[key]
