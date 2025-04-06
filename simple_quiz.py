#Create a multiple-choice quiz with questions about Python, movies, or 
# any fun topic! Display scores at the end and allow the user to play again

#movies_2024 = []
#question1 = ["An action/crime movie released in 2024 featuring Peter Dinklage?"] 10 points, Brothers
#question2 = ["3 Horror movies released in 2024"] 15marks is they give 2 answers from the list below ["It's What's Inside", "Don't move", "Blink Twice", "House of Spoils", "Tarot"]
#question3 = [" A DC movie that was a Bomb at the box office"] 10marks Madam Webb
#question4 = ["A 2024 romantic movie starring Lindsay Lohan"] 10 marks Our little secret
#question5 = ["Third installment in a trilogy about ghosts in New York city"]10 marks Ghostbusters:Frozen empire

question1 = {"An action/crime movie released in 2024 featuring Peter Dinklage?": {"Brothers": 10}}
question2 = {"3 Horror movies released in 2024": ["It's What's Inside", "Don't move", "Blink Twice", "House of Spoils", "Tarot"]}
question3 = {"A DC movie that was a Bomb at the box office": ["Madam Webb"]}
question4 = {"A 2024 romantic movie starring Lindsay Lohan": ["Our little secret"]}
question5 = {"Third installment in a trilogy about ghosts in New York city": ["Ghostbusters:Frozen empire"]}

quiz = []
def movie_guessing_game(question, points=0):
    """Plays a number guessing game with a scoring system."""
    return question[0], sum(question[1] + points[2])

#    attempts = 0
#    score = 0
#    max_attempts = 10  # Set a maximum number of attempts
#
#    print("Welcome to the Movie Guessing Game!")
#    print("I'm thinking of a few questions about movie released in 2024")
#
#    while attempts < max_attempts:
#        try:
#            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the answer: "))
#        except ValueError:
#            print("Invalid input. Please enter an answer.")
#            continue
#
#        attempts += 1
#        return 

#        for question, answer in movie_quiz:
#
#
#        if guess < secret_number:
#            print("Too low!")
#        elif guess > secret_number:
#            print("Too high!")
#        else:
#            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
#            score = 100 - (attempts * 10) # Calculate the score
#            print(f"Your score: {score}")
#            return score
#
#    print(f"You ran out of attempts. The number was {secret_number}.")
#    print(f"Your score: {score}")
#    return score
#
#if __name__ == "__main__":
#    play_number_guessing_game()

        
                                                                                                    