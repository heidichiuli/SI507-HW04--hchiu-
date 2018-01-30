import random

def magic_question():
    current_boolean = True
    while current_boolean == True:
        question = input("What is your question?")
        if question == "quit":
            break
        elif question[-1] != "?":
            print("I'm sorry, I can only answer questions.")
        else:
            list_of_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            print(random.choice(list_of_answers))

magic_question()
