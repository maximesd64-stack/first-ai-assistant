print("==============================")
print(" MY STUDENT ASSISTANT")
print("==============================")

name = input("What is your name? ")
print("Hello", name, "!")

# Main menu of the Student Assistant
choice = input(
    "What do you want to do?\n"
    "1 - Check a grade\n"
    "2 - Calculate an average\n"
    "3 - Get motivation\n"
    "4 - Learn Python\n"
    "Your choice: "
)

if choice == "1":

    grade = float(input("Enter your grade: "))

    if grade >= 16:
        print("Excellent work")
        
    elif grade >= 13
        print("Very good")

    elif grade >= 10:
        print("You passed")

    else:
        print("Keep practising")


elif choice == "2":

    grade1 = float(input("First grade: "))
    grade2 = float(input("Second grade: "))

    average = (grade1 + grade2) / 2

    print("Your average is:", average)


elif choice == "3":

    print("You do not need to know everything today.")
    print("Keep coding, make mistakes, and try again!")


elif choice == "4":

    level = input(
        "What is your Python level? "
        "Beginner, Intermediate or Advanced? "
    ).lower()

    if level == "beginner":

        print("LESSON: Variables")
        print("A variable stores a value.")
        print("Example:")
        print("age = 20")

        print("Exercise:")
        print("Create a variable called age and give it the value 20.")

        answer = input("Your answer: ")
        answer = answer.replace(" ", "")

        if answer == "age=20":
            print("Correct!")

        else:
            print("Not correct.")
            print("Hint: variable = value")


    elif level == "intermediate":

        print("LESSON: Conditions")
        print("Conditions allow your program to make decisions.")
        print("Example:")
        print("if age >= 18:")
        print("    print('Adult')")

        print("Exercise:")
        print("Write a condition that checks if age is greater than or equal to 18.")

        answer = input("Your answer: ")
        answer = answer.replace(" ", "")

        if answer == "ifage>=18:":
            print("Correct!")

        else:
            print("Not correct.")
            print("Hint: use if and >=")


    elif level == "advanced":

        print("LESSON: Functions")
        print("Functions allow you to reuse code.")
        print("Example:")
        print("def hello(name):")
        print("    print('Hello', name)")

        print("Exercise:")
        print("Create a function called is_even that takes n as a parameter.")

        answer = input("Your answer: ")
        answer = answer.replace(" ", "")

        if answer == "defis_even(n):":
            print("Correct!")

        else:
            print("Not correct.")
            print("Hint: use def function_name(parameter):")


    else:

        print("I do not know this level yet.")


else:

    print("I do not understand that choice yet.")


    