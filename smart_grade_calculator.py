# grades lists
assignments = []
amount_of_assignments = []

# caluclation function
def calculation():
    average = sum(assignments)/amount_of_assignments[0]
    average = round(average)
    if average<=49:
        print(f"Your grade is an F at {average}%")
        
    elif 50<=average<=59:
        print(f"You're not failing {average}")
# Ask the amount of assignments
amount_of_assignments.append(int(input("How many assignments do you have?")))

# ask results in assignments
for i in range(amount_of_assignments[0]):
        assignments.append(int(input("Enter your grades:")))
        
# call caluclation function
calculation()