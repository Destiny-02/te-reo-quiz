# Te Reo Quiz Program, 24/05, Destiny Li

# Version 3 (Component 1, 2 and 3 added)

# Component 1 - Ask user each question, give corresponding options,
# check that their response matches the correct answer and give appropriate feedback

# Component 2 added - Allow user to quit at any time and play again if the quiz has ended
# Output introduction, ask user for their name and give results when the quiz has ended

# Component 3 added - Check for valid yes/no, name amd option number responses


# Checks for a yes / no response
# Will continue asking question until a valid response has been given


def yes_no_check(question):

    valid = False
    while not valid:

        response = input(question)

        if response.lower() == "yes" or response.lower() == "y": # these are all valid possibilities for a "yes" response
            response = "yes"
            return response

        elif response.lower() == "no" or response.lower() == "n": # these are all valid possibilities for a "no" response
            response = "no"
            return response

        else:
            print("Please enter a Y/N response")


# Checks for a valid a user name
# A valid user name should have between 2 and 30 characters (inclusive) and should contain only letters and spaces.
# The user name will be returned with the start of each word capitalised


def name_check(question, MIN_LENGTH, MAX_LENGTH):

    valid = False
    while not valid:
        user_name = input(question)
        user_name = user_name.title()

        # to check if the user's name is greater than 2 characters AND contains only letters and spaces
        # modified from https://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
        if MIN_LENGTH <= len(user_name) <= MAX_LENGTH and all(letter.isalpha() or letter.isspace() for letter in user_name) == True:
            return user_name
        else:
            print("Your name must be between {} and {} characters. Only letters and spaces allowed.".format(MIN_LENGTH, MAX_LENGTH))


# Checks for a valid response (a number that is in the option range or 0)


def num_check(num_options):

    valid = False

    while not valid:

            try:
                response = int(input("Enter an answer or press 0 to stop answering questions "))

                # -1 because variable was increased by one after the last option was printed
                if 0 <= response <= num_options - 1:
                    return response
                else:
                    print("not in range!")

            except ValueError:
                print("not a number")


if __name__ == "__main__":

    MIN_LENGTH = 2
    MAX_LENGTH = 30
    keep_going = "yes"
    while keep_going == "yes":

        # setting up all the questions, options and answers
        questions = ["What is the term for ‘Maori’ language?",
                     "What is the Maori term for ‘tribe’ or ‘mob’?",
                     "What is the term for the formal welcome, where two individuals press their nose together?",
                     "Who is the ‘demi-god’ or the ‘great creator’ who fished NZ out from the sea?",
                     "What is the name for the traditional Maori method of cooking?",
                     "What is the Maori term for ‘blue’?",
                     "What is the Maori term for “one hundred”?"]
        options = [["Te Rex", "Hangi", "Hongu", "Te Reo"],
                   ["Mihi", "Iwi", "Awi", "Hapu"],
                   ["Hongi", "Haka", "Hangi", "Huka"],
                   ["Zeus", "Hercules", "Maui", "Maori"],
                   ["Roast", "Hangi", "Hongi", "Bake"],
                   ["Kikorangi", "Kakariki", "Karaka"],
                   ["kotahi mano", "kotahi rau"]]
        answers = [4, 2, 1, 3, 2, 1, 2]

        # to keep track of which question the program is asking
        num_questions = 0
        num_correct = 0

        user_name = name_check("What is your name? ", MIN_LENGTH, MAX_LENGTH)
        print("Hi {}".format(user_name))
        print("Welcome to quiz night!"
              "\nYou will be presented with {} questions"
              "\nEnter the appropriate number to answer the question."
              "\nGood luck! \n".format(len(questions)))

        # prints each question
        for question in questions:
            option_number = 1
            print(question)

            # prints each option related to the current question
            for option in options[num_questions]:
                print("{}. {}".format(option_number, option))
                option_number += 1

            print()
            response = num_check(option_number)

            # stop asking questions if the user has pressed the 0
            if response == 0:
                break

            # gives feedback based on response and outputs the correct option number and option word
            if response == answers[num_questions]:
                print("Well Done. The correct answer was {}, {}"
                      .format(answers[num_questions], options[num_questions][answers[num_questions] - 1]))
                num_correct += 1
            else:
                print("Incorrect. The correct answer was {}, {}"
                      .format(answers[num_questions], options[num_questions][answers[num_questions] - 1]))
            print()
            num_questions += 1

        print("\n{}: You scored {} out of {}.\nThanks for playing!".format(user_name, num_correct, num_questions))

        keep_going = yes_no_check("Play again Y/N? : ")
        print()
