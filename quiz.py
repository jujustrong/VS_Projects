import time
import random

# Write a program that loops through the questions and adds 1 to the score if the player answers correctly
# and 0 if they answer incorrectly
# Print the score with a message of your choice at the end. You may also print a different message based on how well the user did.

class Dict_create(dict):
    def __init__(self) -> None:
        self = dict()
    def add(self, key, value):
        self[key] = value
    def remove(self, key):
        del[key]

class Quiz():
    
    def name_quiz(self):
        i = True
        while i:
            self.quiz_name = input("What would you like to name the quiz? ")
            time.sleep(1)
            save_name = input(f"Save quiz name as {self.quiz_name}?\nEnter 1 for yes or 2 for no: ")
            if save_name == 1:
                print(f"{self.quiz_name} has been saved")
                i = False
            elif save_name == 2:
                i = True
            else:
                print("Please enter 1 or 2")
                i = True
        return self.quiz_name

    def quiz_maker(self):
        i = True
        self.questions = []
        while i:
            quiz_question = input("Enter a QUESTION (enter 'done' if finished): \n")
            if quiz_question == "done":
                print("Here are the quiz questions and answers we have so far:")
                for q in self.questions:
                    print(q['question'], q['answer'])
                time.sleep(1.5)
                confirm = input("Complete quiz? Enter 1 for YES and 2 for NO: ")
                if confirm == "1":
                    print("Your quiz has been saved")
                    i=False
                elif confirm == "2":
                    i=True
                else:
                    print("Please enter a 1 or 2")
                    i=True
            elif quiz_question.lower() != 'done':
                quiz_answer = input("Enter the ANSWER for the question: \n")
                question = Dict_create()
                question.add("question",quiz_question)
                question.add("answer",quiz_answer)
                self.questions.append(question)
                i=True
            else:
                print("please enter a question or enter 'done'")
                i=True
        return self.questions


    def quizzy(self):
        print(f"Today you will be taking the '{self.name}' quiz")
        time.sleep(1)
        print("Answer the questions to the best of your ability. You will recieve a score at the end. Good luck!")
        time.sleep(1.5)
        score = 0
        total = 0
        for q in self.questions:                                        #Accessing each individual set of dicts in our list
            time.sleep(1)
            answer = input(f"{q['question']}: ")                        #Taking a single set and printing/accessing the value of the "question" key
            if answer.lower() == q['answer'].lower():                   #Checking if user answer matches value in "answer" key of the current set
                print("That's Correct!")
                score += 1
                total += 1
            else:
                print("Sorry that's Incorrect...")
                total += 1
        time.sleep(1)
        print("Let's calculate your final score!")
        time.sleep(1)
        final_score = (score/total) * 100
        print(f'Your final score is: {final_score:.0f}')


my_quiz = Quiz()
my_quiz.quiz_maker()
my_quiz.quizzy()