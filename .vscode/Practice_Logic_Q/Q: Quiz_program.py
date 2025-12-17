# Q: Quiz program:

# Question 1
q1 = """If a train travels 60 km in 1 hour, how long will it take to travel 150 km at the same speed?

a) 2 hours
b) 2.5 hours
c) 3 hours
d) 1.5 hours"""

# Question 2
q2 = """What is the value of(12×3) − (8÷2)?

a) 30
b) 32
c) 34
d) 28"""

# Question 3
q3 = """
x = 5
y = 10
x, y = y, x
print(x, y)

a) 5 10
b) 10 5
c) Error
d) None
"""

# Question 4
q4 = """How many months in a year have 28 days?

a) 1
b) 2
c) 6
d) 12"""

# Question 5
q5 = """Which planet in our solar system has the shortest day?

a) Earth
b) Mars
c) Jupiter
d) Venus"""


# main block of code
def Quiz(name, questions):
    print("\n""Welcome to the Quiz""\n\n""Quiz begins now""\n")
    score = 0
    for i in questions:
        print()
        print(i)

        skip = input("Do you want to skip this Question? (Y/N): ")
        skip.lower()
        if skip == "y":
            continue

        ans = input("Enter the answer to question as (a/b/c/d): ")

        if ans == questions[i]:
            print("Nice! your answer is correct, bingo 1 point")
            score += 1
            print(f"Your score currently is:{score}")
        else:
            print("Sorry :(, your answer is wrong, lost 1 point")
            score -= 1
            print(f"Your score currently is:{score}")
        
        quit = input("Do you wanna Quit the Quiz? (Y/N): ")
        quit.lower()
        if quit == "y":
            break
    return (f"Your Final score is:{score}")


questions = {q1 : "b", q2 : "c", q3 : "b", q4 : "d", q5 : "c"}
name = input("What is your Name? ")
print(Quiz(name, questions))
