class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define your list of questions
questions = [
    Question("What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n", "b"),
    Question("Who wrote 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Jane Austen\n(c) Charles Dickens\n", "a"),
    Question("What is the chemical symbol for water?\n(a) Wo\n(b) Wa\n(c) H2O\n", "c")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_quiz(questions)
