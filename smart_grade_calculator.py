# Grades lists
amount_of_assignments = []
assignments = []

# Ask the amount of assignments
def get_amount_of_assignments():
    while True:
        try:
            amount_of_assignments.append(int(input("How many assignments do you have?").strip()))
            get_assignments()
        except:
            print("Enter a valid answer")
get_amount_of_assignments()
# ask results in assignments
def get_assignments():
    for x in range(amount_of_assignments[0]):
        while True:
            try:
                assignment = (int(input("Enter your grades:").strip()))
                if 0<=assignment<=100:
                    assignments.append(assignment)
                    break
            except:
                print("Answer a valid answer")
    calculation()
    
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
    restart()


def restart():
    while True:
        restart_choice = input("Do you want to do another calculation [y]es or [n]o").strip()
        if restart_choice == "y":
            average = 0
            amount_of_assignments.clear()
            assignments.clear()
            get_amount_of_assignments()
            break
        elif restart_choice == "n":
            print("Bye")
            break
        else:
            print("Enter a valid answer")
            


