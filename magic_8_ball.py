import random

name = input("Enter a name: ")
question = input("Enter a question: ")
answer = ""

should_exit = False #way of stopping the program

if name == "":
    print("Question:", question)
elif question == "":
    print("You have not asked a question, ", name)
    should_exit = True

if not should_exit:
    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Yes-Definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer = "Error"

    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)
