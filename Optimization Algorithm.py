def test():
    total_points = 0
    print("Hello! What is your name")
    name = input("Name: ")
    print("Hello" + str(name) + ", TripleT will be asking you some questions today to find out your risk level")
    print("How old are you?")
    age = input("Age: ")
    question_prompts = [
        "What profession sector do you work in?\n(a) Healthcare\n(b) Business, consulting and management\n(c)  "
    ]
    if age >= 70:
        total_points += 5
    elif age >= 51:
        total_points +=





