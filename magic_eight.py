import random

def magic_question():
    question = input("What is your question?")
    list_of_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    while question != "quit"
        if question[-1] == "?":
            return random.choice(list_of_answers)
        else:
            return "I'm sorry, I can only answer questions."
