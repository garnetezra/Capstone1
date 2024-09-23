# Define initial nested dictionary
students_info = {
    1: {"Name": "Adit", "Rate": 30000, "Sessions": 4, "Grade": 4, "Attendance": 0},
    2: {"Name": "Akmal", "Rate": 75000, "Sessions": 12, "Grade": 5, "Attendance": 0},
    3: {"Name": "Yehezkiel", "Rate": 20000, "Sessions": 4, "Grade": 4, "Attendance": 0},
    4: {"Name": "Aswin", "Rate": 50000, "Sessions": 4, "Grade": 4, "Attendance": 0},
    5: {"Name": "Eezar", "Rate": 25000, "Sessions": 4, "Grade": 3, "Attendance": 0},
    6: {"Name": "Gwen", "Rate": 20000, "Sessions": 4, "Grade": 3, "Attendance": 0},
    7: {"Name": "Jeano", "Rate": 50000, "Sessions": 4, "Grade": 5, "Attendance": 0},
    8: {"Name": "Justin", "Rate": 45000, "Sessions": 8, "Grade": 5, "Attendance": 0},
    9: {"Name": "Jovan", "Rate": 20000, "Sessions": 4, "Grade": 4, "Attendance": 0},
    10: {"Name": "Michele", "Rate": 20000, "Sessions": 4, "Grade": 3, "Attendance": 0},
    11: {"Name": "Nay", "Rate": 35000, "Sessions": 8, "Grade": 5, "Attendance": 0},
    12: {"Name": "Oni", "Rate": 20000, "Sessions": 4, "Grade": 4, "Attendance": 0},
    13: {"Name": "Willi", "Rate": 50000, "Sessions": 4, "Grade": 5, "Attendance": 0},
}

# Helper function to limit input attempts and return to the main menu after 3 failed attempts
def limited_input(prompt, expected_type, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        try:
            # Get user input
            user_input = input(prompt)
            
            # Convert input to the expected type
            if expected_type == int:
                user_input = int(user_input)
            elif expected_type == float:
                user_input = float(user_input)
            
            # If input is valid, return the value
            return user_input
        except ValueError:
            # Increment attempts if invalid input
            attempts += 1
            print(f"Invalid input. Please enter a valid {expected_type.__name__}. Attempts left: {max_attempts - attempts}")

    # If 3 attempts are exhausted, force return to the main menu
    print("Too many invalid attempts. Returning to the main menu.")
    return main_menu()

def display_student_table(students):
    # Initialize a dictionary to store the maximum lengths for each column
    max_lengths = {
        "Index": len("Index"),
        "Name": len("Name"),
        "Rate": len("Rate"),
        "Sessions": len("Sessions"),
        "Grade": len("Grade"),
        "Attendance": len("Attendance"),
        "Payment Due": len("Payment Due")
    }

    # Find the maximum lengths dynamically based on the student data
    for idx, student in students.items():
        max_lengths["Index"] = max(max_lengths["Index"], len(str(idx)))
        max_lengths["Name"] = max(max_lengths["Name"], len(student["Name"]))
        max_lengths["Rate"] = max(max_lengths["Rate"], len(f"Rp{student['Rate']:,}"))
        max_lengths["Sessions"] = max(max_lengths["Sessions"], len(str(student["Sessions"])))
        max_lengths["Grade"] = max(max_lengths["Grade"], len(str(student["Grade"])))
        max_lengths["Attendance"] = max(max_lengths["Attendance"], len(str(student["Attendance"])))
        max_lengths["Payment Due"] = max(max_lengths["Payment Due"], len(f"Rp{student['Rate'] * student['Attendance']:,}"))

    # Create the header with dynamic widths
    print(f"{'Index':<{max_lengths['Index']}} | {'Name':<{max_lengths['Name']}} | {'Rate':<{max_lengths['Rate']}} | {'Sessions':<{max_lengths['Sessions']}} | {'Grade':<{max_lengths['Grade']}} | {'Attendance':<{max_lengths['Attendance']}} | {'Payment Due':<{max_lengths['Payment Due']}}")

    # Loop through students and print the data with dynamic column width
    for idx, student in students.items():
        name = student["Name"]
        rate = f"Rp{student['Rate']:,}"
        sessions = student["Sessions"]
        grade = student["Grade"]
        attendance = student["Attendance"]
        payment_due = f"Rp{student['Rate'] * student['Attendance']:,}"

        print(f"{idx:<{max_lengths['Index']}} | {name:<{max_lengths['Name']}} | {rate:<{max_lengths['Rate']}} | {sessions:<{max_lengths['Sessions']}} | {grade:<{max_lengths['Grade']}} | {attendance:<{max_lengths['Attendance']}} | {payment_due:<{max_lengths['Payment Due']}}")

# Run the display function
def display_students():
    while True:
        print("\nDisplay Students Menu:")
        display_student_table(students_info)
        print("\n1. Filter by Grade")
        print("2. Sort by Attendance")
        print("3. Return to Main Menu")
        
        choice = input("Enter the number of the submenu you want to run: ")
        
        if choice == '1':
            try:
                grade_filter = int(input("\nEnter the grade to filter by: "))
                filtered_students = {idx: student for idx, student in students_info.items() if student['Grade'] == grade_filter}
                
                if filtered_students:
                    print(f"\nDisplaying Students in Grade {grade_filter}:\n")
                    display_student_table(filtered_students)
                else:
                    print(f"\nNo students found in Grade {grade_filter}.")
            except ValueError:
                print("\nPlease enter a valid integer for the grade.")

        elif choice == '2':
            # Sort by Attendance
            sorted_students = sorted(students_info.items(), key=lambda x: x[1]["Attendance"], reverse=True)
            print("\nStudents sorted by attendance:\n")
            sorted_students_dict = {idx: student for idx, student in sorted_students}
            display_student_table(sorted_students_dict)

        elif choice == '3':
            print("\nReturning to the main menu...")
            break

        else:
            print("\nInvalid input, please select a valid option.")


# Add Student (Registration)
def student_registration():
    name = input("Enter student's name: ")
    rate = limited_input("Enter student's rate (positive integer): ", int)
    sessions = limited_input("Enter number of sessions (positive integer): ", int)
    grade = limited_input("Enter student's grade (positive integer): ", int)
    
    if name and rate > 0 and sessions > 0 and grade > 0:
        new_index = len(students_info) + 1
        students_info[new_index] = {"Name": name, "Rate": rate, "Sessions": sessions, "Grade": grade, "Attendance": 0}
        print("\nUpdated Student List:")
        display_students()
    else:
        print("All inputs must be positive integers.")

# Remove Student (Cancellation)
def student_cancellation():
    print()
    display_student_table(students_info)  # Display the list of students
    student_index = limited_input("\nEnter the index of the student to cancel: ", int)  # Get student index input
    if student_index in students_info:
        # Check attendance before generating the invoice
        if students_info[student_index]["Attendance"] > 0:
            generate_invoice(student_index)  # Generate an invoice for the student
        else:
            print(f"\nNo invoice needed for {students_info[student_index]['Name']} as their attendance is 0.")
        
        del students_info[student_index]  # Remove the student from the records
        print("\nUpdated Student List:")
        display_students()  # Display the updated list of students
    else:
        print("Invalid index!")  # Handle invalid index input

# update attendance
def reccord_attendance():
    print()
    display_student_table(students_info)
    index = limited_input("Enter the student's index to Record Attendance: ", int)

    if index in students_info:
        attempts = 0
        while attempts < 2:  # Allow 2 attempts
            attendance_to_add = limited_input("Enter attendance to add: ", int)
            if attendance_to_add + students_info[index]["Attendance"] <= students_info[index]["Sessions"]:
                students_info[index]["Attendance"] += attendance_to_add
                print(f"Attendance updated for {students_info[index]['Name']}. Total attendance is now {students_info[index]['Attendance']}.")
                return  # Exit the function after successful update
            else:
                max_attendance = students_info[index]["Sessions"] - students_info[index]["Attendance"]
                print(f"\nCannot add attendance. You can only add up to {max_attendance} more sessions.")
                attempts += 1
                if attempts < 2:  # Only prompt again if there's still an attempt left
                    print("\nPlease try again.")
        
        print("\nToo many invalid attempts")
    else:
        print("\nStudent not found.")


# Generate Invoice
def generate_invoice(student_index=None):
    print()
    if student_index is None:
        display_student_table(students_info)  # Show the list of students
        student_index = limited_input("Enter the index of the student to generate invoice for: ", int)
        
    if student_index in students_info:
        student = students_info[student_index]
        
        if student["Attendance"] > 0:  # Check if attendance is greater than 0
            amount_due = student["Rate"] * student["Attendance"]
            print(f"\n--- Invoice for {student['Name']} ---")
            print(f"Rate per session: Rp{student['Rate']:,.0f}")
            print(f"Total attendance: {student['Attendance']}")
            print(f"Total amount due: Rp{amount_due:,.0f}")
            print("-------------------------")
            # Reset payment due and attendance after generating invoice
            student["Attendance"] = 0
        else:
            print(f"\nNo invoice needed for {student['Name']} as their attendance is 0.")  # No invoice message
    else:
        print("\nInvalid student index!")



# Filter students by grade
def filter_by_grade():
    grade = limited_input("Enter the grade to filter by: ", int)
    print(f"\nStudents in Grade {grade}:")
    for index, student in students_info.items():
        if student["Grade"] == grade:
            print(f"{index}: {student['Name']}")

# Sort students by attendance
def sort_by_attendance():
    sorted_students = sorted(students_info.items(), key=lambda x: x[1]["Attendance"], reverse=True)
    print("\nStudents sorted by attendance:")
    for index, student in sorted_students:
        print(f"{index}: {student['Name']} - Attendance: {student['Attendance']}")

def prompt_return_to_menu():
    input("\nPress Enter to return to the main menu...")


# Main Menu Function
def main_menu():
    print("\nMenu List:")
    print("1. Display Students")
    print("2. Student Registration")
    print("3. Student Cancellation")
    print("4. Reccord Attendance")
    print("5. Generate Invoice")
    print("6. Exit")

# Main Program Loop
def run():
    while True:
        main_menu()
        menu = limited_input("Enter the menu number to run: ", int)
        if menu == 1:
            display_students()
        elif menu == 2:
            student_registration()
        elif menu == 3:
            student_cancellation()
        elif menu == 4:
            reccord_attendance()
        elif menu == 5:
            generate_invoice()
        elif menu == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
run()
