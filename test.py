class Question:
     def __init__(self, prompt: object, answer: object) -> object:
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What profession sector are you in?\n(a) Healthcare\n(b)Business",
     "How old are you? Select a range\n\n\n\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[0]), "b")]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "points from", len(questions), " questions")

run_quiz(questions)
