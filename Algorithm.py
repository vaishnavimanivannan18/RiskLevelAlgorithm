#setting initial value of variable
score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to the classification algorithm for risk prediction! 
You will be presented with 2 questions regarding your age and profession.
Enter the appropriate number or letter to answer the question
Good luck!""".format(name))

#Question1
print("""What is your age category?
1. 13-35 
2. 36-50
3. 51-69 
4. 70-100""")

answer1 = "1"
answer2 = "2"
answer3 = "3"
answer4 = "4"

response1 = input("Your answer is:")

if response1 == answer1:
    score += 2
elif response1 == answer2:
    score += 3
elif response1 == answer3:
    score += 4
else:
    score += 5

print("Your current score is " + str(score))

#Question 2
print("""What sector of profession are you in?
a. Student/School
b. Public workers (chefs, labourers, bartenders etc)
c. Education (teachers, professors)
d. Healthcare (doctors, nurses)""")

answertwo1 = "a"
answertwo2 = "b"
answertwo3 = "c"
answertwo4 = "d"

response2 = input("Your answer is:")

if response2 == answertwo1:
    score += 2
elif response2 == answertwo2:
    score += 3
elif response2 == answertwo3:
    score += 4
else:
    score += 5

#Printing the final results
print("Your current score is " + str(score))

print("Your total score is " + str(score))
if score >= 7:
    print("You fall in the higher risk end and hence will be prioritized to get vaccinated!")

print("Thank you for taking part in this {}!".format(name))

