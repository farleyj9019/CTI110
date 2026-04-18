# Justin Farley
# 4/15/2026
# P4HW1
# program will use a loop. Also, after displaying score average (after dropping lowest score) , the program is to display a letter grade for the calculated average.

# Ask for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Empty list
scorenumbers = []

# Collect scores
for score_num in range(1, num_scores + 1):
    score = float(input(f"Enter score #{score_num}: "))

    # Validate score
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_num} again: "))
    scorenumbers.append(score)

# lowest score
lowest_score = min(scorenumbers)

# Empty list
Modifiedlist = []

# Copy scores into new list
for score in scorenumbers:
    Modifiedlist.append(score)

# Remove lowest score
Modifiedlist.remove(lowest_score)

# Find total of modified list
total = 0
for score in Modifiedlist:
    total = total + score

# Find the average
average_score = total / len(Modifiedlist)

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
else:
    if average_score >= 80:
        letter_grade = "B"
    else:
        if average_score >= 70:
            letter_grade = "C"
        else:
            if average_score >= 60:
                letter_grade = "D"
            else:
                letter_grade = "F"

# Display results
print("--------------Results--------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {Modifiedlist}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------------")