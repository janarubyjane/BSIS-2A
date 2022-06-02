# Members: Padasas, Jeannah Jean S. & Porras, Ma. Alexia Louise ( BSIS - 2AB )

import random
import os
import time

def add(x, y):
    return x + y

def subtrct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y

while True:
    os.system("cls")
    print("  MATH TUTOR  \n\n")
    print("1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division\n")

    choice = input("Choose operation: ")
    probNum = int(input("How many problems?: "))
    i = 0
    score = 0
    # The user is asked to select an operation and the number of problems they want to solve.

    if choice in ('1', '2', '3', '4'):
        # ADDITION 
        if choice == '1': 
            print("\n")
            # while loop to limit the number of questions based on the problems inputed by the user.
            while i < probNum:
                # Generating two random numbers and adding them together.
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                
               # Asking the user to input an answer.
                print("What is the sum of " + str(num1) + " and " + str(num2) + "?")
                answer = float(input("Answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    # Printing the correct answer.
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            # Printing the score of the user.
            print("score: " + str(score) + "/" + str(probNum))
            break
        
        elif choice == '2': 
            # SUBTRACTION 
            print("\n")
            while i < probNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(probNum))
            break
        
        elif choice == '3': 
            # MULTIPLICATION 
            print("\n")
            while i < probNum:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(probNum))
            break
        
        elif choice == '4': 
            # DIVISION
            print("\n")
            while i < probNum:
                num1 = round(float(random.randint(0, 9)),2)
                num2 = round(float(random.randrange(2, 10, 2)), 2)
                num3 = dividiby(num1, num2)

                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct\n")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("\n")
                i += 1
            print("Score: " + str(score) + "/" + str(probNum))
            break

else:
    print("Invalid input")