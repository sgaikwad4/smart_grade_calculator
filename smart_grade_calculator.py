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
        print(f"Your grade is a C- at {average}%")
        
    elif 60<=average<=66:
        print(f"Your grade is a C at {average}%")
        
    elif 67<=average<=72:
        print(f"Your grade is a C+ at {average}%")
        
    elif 73<=average<=85:
        print(f"Your grade is a B at {average}%")
    
    else:
        print(f"Your grade is an A at {average}%")
    
# Ask the amount of assignments
while True:
    amount_of_assignments.append(int(input("How many assignments do you have?")))

# ask results in assignments
for i in range(amount_of_assignments[0]):
    assignments.append(int(input("Enter your grades:")))
        
# call caluclation function
calculation()