

# Write a program that determines the letter grade for a course according to the following scale:

# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60

# Assignment
# Start by completing the core requirements, then when that part is complete, if you have time, 
# see if you can complete some of the stretch challenges as well.

# Please work through the requirements in order rather than jumping ahead to more complicated steps,
# to ensure that everyone is following the concepts.

# CORE REQUIREMENTS
# Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the 
# appropriate letter grade. (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

# Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. 
# Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them. 
# If not, display a different message to encourage them for next time.

# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, 
# instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the 
# whole series of if-elif-else statements, have a single print statement that prints the letter grade once.

# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60


grade_P = input("Enter your percentage:")
grade_P = float(grade_P)
last_digit = grade_P % 10
sign = ""


if grade_P >= 93:
    sign = ""
else: 
    grade_P < 60 and grade_P >= 0
    sign = ""


if last_digit >= 7:
    sign = "+"
else:
    last_digit < 3
    sign = "-"


if grade_P >= 90 and grade_P <= 93:
    letter = "A"
    grade_P = (f"{letter}{sign} \nBravo, you passed!")
elif grade_P >= 90:
    letter = "A"
    grade_P = (f"{letter} \nBravo, you passed!")
elif grade_P >= 80 and grade_P < 90:
    letter = "B"
    grade_P = (f"{letter}{sign} \nBravo, you passed!")
elif grade_P >= 70 and grade_P < 80:
    letter = "C"
    grade_P = (f"{letter}{sign} \nBravo, you passed!")
elif grade_P >= 60 and grade_P < 70:
    letter = "D"
    grade_P = (f"{letter}{sign} \nWith a little more effort, you'll make it. Better luck next time.")
elif grade_P < 60 and grade_P >= 0:
    letter = "F"
    grade_P = (f"{letter} \nYou've got to show more commitment")
else:
    grade_P = ("YOU WILL NEVER MAKE IT IN THIS LIFE, BITCH-ASS DICK-HEAD!!! \nWord of advice?... Try the next life.")
print(grade_P)



# Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, 
# you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

# After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. 
# Then, display both the grade letter and the sign in one print statement.

# Hint: To get the last digit, you could divide the number by 10, and get the remainder. 

# Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.


# Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle 
# them correctly.


# if grade_P >= 90:
#     grade_P = "A"
# elif grade_P >= 80 and grade_P < 90:
#     grade_P = "B"
# elif grade_P >= 70 and grade_P < 80:
#     grade_P = "C"
# elif grade_P >= 60 and grade_P < 70:
#     grade_P = "D"
# elif grade_P < 60:
#     grade_P = "F"
#     print(grade_P)
# else: 

# if grade_P