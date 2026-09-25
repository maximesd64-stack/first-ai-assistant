name = input("What is your name? ")
degree = input("What is your degree? ")
print("Welcome", name, "! You are studying", degree)

  grades = float(input("what is ur grades?"))
      if grades >= 16:
          print("Perfect")
      elif grades >= 13
          print("Very good")
      elif grades >=10:
          print("U pass good job")
      else:
          print("Practice more")
  grade1 = float(input("what is ur first grade ?"))
  grade2 = float(input("what is ur first grade ?"))
  moy_grade = (grade1 + grade2) / 2
  print(moy_grade)

 stuying_time = int(input("How many hours do you work at home? "))

 if stuying_time == 0:
     print("You need to work at home!!!")

 elif stuying_time <= 2:
     print("Continue like that")

 else:
     print("Take some rest....")

choise = input(
    "What u want to do ?\n"
    "1 - Check a grade\n"
    "2 - Calculate an average\n"
    "3 - Studying time"
    "ur choise:"
)
if choise == "1":
    grades = float(input("what is ur grades?"))
    if grades >= 15:
         print("Perfect")
    elif grades >=10:
         print("u pass good job")
    else:
         print("practice more")
elif choise == "2":
    grade1 = float(input("what is ur first grade ?"))
    grade2 = float(input("what is ur first grade ?"))
    moy_grade = (grade1 + grade2) / 2
    print(moy_grade)
elif choise == "3":
    stuying_time = int(input("How many hours do you work at home? "))

    if stuying_time == 0:
        print("You need to work at home!!!")

    elif stuying_time <= 2:
        print("Continue like that")

    else:
        print("Take some rest....")