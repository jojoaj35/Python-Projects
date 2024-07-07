print("Welcome to my computer quiz")

points = 0

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Come again next time")
    quit()
else:
    print("Okay, let's play")

# Question 1
answer = input("Real-life arithmetic and Computer-arithmetic are the same all the time. For example, if you multiply two positive integers you will get a positive integer all the time for computer arithmetic. (True/False) ")
if answer.lower() == "false":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

# Question 2
answer = input("In this course, we will learn about the underlying machine from the programmer's perspective. (True/False) ")
if answer.lower() == "true":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

# Question 3
answer = input("The C standards do not precisely define which type of right shift should be used with signed numbers—either arithmetic or logical shifts may be used. This unfortunately means that any code assuming one form or the other will potentially encounter portability problems. (True/False) ")
if answer.lower() == "true":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

# Question 4
answer = input("An arithmetic right shift fills the left end with k repetitions of the least significant bit. (True/False) ")
if answer.lower() == "false":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

# Question 5
answer = input("Argument x is [01100011]. If you apply the right shift (logical and k = 4) on it, then it becomes [00000110]. (True/False) ")
if answer.lower() == "true":
    print('Correct!')
    points += 3
else:
    print('Incorrect!')

# Question 6
answer = input("When we represent negative numbers at the machine level, one important feature to note is that the ranges are not symmetric—the range of negative numbers extends one further than the range of positive numbers. (True/False) ")
if answer.lower() == "true":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

# Question 7
answer = input("Bits to Unsigned(positive integer) transformation of [1111] is 13. (True/False) ")
if answer.lower() == "false":
    print('Correct!')
    points += 5
else:
    print('Incorrect!')

print(f"Your total points: {points}")

print ("Thank you for playing")
