# Kathryn Hofmeister
# 7/4/25
# P4HW1
# This program lets the user enter multiple scores, drops the lowest,
# calculates the average, and displays the corresponding letter grade.

# Ask the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store valid scores
scores = []

# Loop to collect scores
for i in range(1, num_scores + 1):
    while True:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break  # exit the inner loop if the score is valid
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")

# Calculate lowest score and remove it
lowest = min(scores)
scores.remove(lowest)

# Calculate average
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-------------------------------")
