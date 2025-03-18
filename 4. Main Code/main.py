from login_user import LoginUser
from common import Student,students, Professor, professors, Course, courses, Grades, grades
import getpass
import shutil

def main_menu():

    while True:
        columns = shutil.get_terminal_size().columns
        print("=================================".center(columns))
        print("Welcome to CheckMyGrade APP!".center(columns))
        print("================================".center(columns))
        email_id = input("Enter your Email ID: ").strip()
        password = getpass.getpass("Enter you password: ")
        login = LoginUser(email_id, password)
        status, role = login.login()

        if not status:
            print("Login failed. Please try again.")
            continue
        
        # Main menu after successful login
        while True:
            print("\n")
            print("1. Go to main menu")
            print("2. Change password")
            print("3. Logout")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                if role == "admin":
                    admin_menu(role, email_id)
                elif role == "professor":
                    professor_menu(role, email_id)
                elif role == "student":
                    student_menu(role, email_id)
            elif choice == "2":
                login.change_password()    
            elif choice == "3":
                login.logout()
                break
            else:
                print("Invalid choice, please enter again.") 

def admin_menu(role, email_id):
    while True:
        print("\nAdmin Menu:")
        print("1. Display Student Records")
        print("2. Display Professor Records")#sort
        print("3. Display Course Records")#sort
        print("4. Display Grades Records")#sort
        print("5. Add/Delete/Modify Student")
        print("6. Add/Delete/Modify Professor")
        print("7. Add/Delete/Modify Course")
        print("8. Add/Delete/Modify Grades")
        print("9. Generate Grade Report")
        print("10. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1": # have tested
            print("\n Display Student Records Menu:")
            print("1. Display all students' details")
            print("2. Display chosen student's details")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                sort_by = input("Enter the sort by (student_id, first_name, last_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                students[list(students.keys())[0]].display_all_students_records(sort_by, reverse)

            elif sub_choice == "2":
                students[list(students.keys())[0]].display_chosen_student_records()

            elif sub_choice == "3":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "2": # have tested
            print("\n Display Professor Records Menu:")
            print("1. Display all professors details")
            print("2. Display chosen professor details")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                sort_by = input("Enter the sort by (professor_id, name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                professors[list(professors.keys())[0]].display_all_professors_records(sort_by, reverse)

            elif sub_choice == "2":
                professors[list(professors.keys())[0]].display_chosen_professor_records()

            elif sub_choice == "3":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "3": # have tested
            print("\n Display Course Records Menu:")
            print("1. Display all courses details")
            print("2. Display chosen course details")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                sort_by = input("Enter the sort by (course_id, course_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                courses[list(courses.keys())[0]].display_all_courses_records(sort_by, reverse)

            elif sub_choice == "2":
                courses[list(courses.keys())[0]].display_chosen_course_records()

            elif sub_choice == "3":
                continue # Return to previous menu
            
            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "4": # have tested
            print("\n Display Grades Records Menu:")
            print("1. Display all grades details")
            print("2. Display chosen grade details")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                sort_by = input("Enter the sort by (student_id, course_id, grades, marks): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                grades_instance = Grades()
                grades_instance.display_all_grades_records(sort_by, reverse)

            elif sub_choice == "2":
                grades[list(grades.keys())[0]].display_chosen_grade_records()

            elif sub_choice == "3":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")

        elif choice == "5":
            print("\n Add/Delete/Modify Student Menu:")
            print("1. Add new student")
            print("2. Delete student")
            print("3. Modify student details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                student_instance = Student()
                student_instance.add_new_student()

            elif sub_choice == "2":
                student_instance = Student()
                student_instance.delete_student()

            elif sub_choice == "3":
                student_instance = Student()
                student_instance.modify_student_records(role, email_id)

            elif sub_choice == "4":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "6":
            print("\n Add/Delete/Modify Professor Menu:")
            print("1. Add new professor")
            print("2. Delete professor")
            print("3. Modify professor details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                professor_instance = Professor()
                professor_instance.add_new_professor()

            elif sub_choice == "2":
                professor_instance = Professor()
                professor_instance.delete_professor()

            elif sub_choice == "3":
                professor_id = input("Enter the professor ID to modify: ").strip()
                professor_instance = Professor()
                professor_instance.modify_professor_details(professor_id)

            elif sub_choice == "4":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "7":
            print("\n Add/Delete/Modify Course Menu:")
            print("1. Add new course")
            print("2. Delete course")
            print("3. Modify course details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                course_instance = Course()
                course_instance.add_new_course()
                
            elif sub_choice == "2":
                course_instance = Course()
                course_instance.delete_course(role, email_id)

            elif sub_choice == "3":
                course_instance = Course()
                course_instance.modify_course(role, email_id)

            elif sub_choice == "4":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "8":
            print("\n Add/Delete/Modify Grades Menu:")
            print("1. Add new grade")
            print("2. Delete grade")
            print("3. Modify grade details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                grades_instance = Grades()
                grades_instance.add_new_grade(role, email_id)

            elif sub_choice == "2":
                grades_instance = Grades()
                grades_instance.delete_grade(role, email_id)

            elif sub_choice == "3":
                grades_instance = Grades()
                grades_instance.display_all_grades_records(role, email_id)

            elif sub_choice == "4":
                continue # Return to previous menu
            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "9": # have tested
            print("\n Generate Grade Report Menu:")
            print("1. Generate grade report for a student")
            print("2. Generate grade report for a professor")
            print("3. Generate grade report for a course")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                grades_instance = Grades()
                grades_instance.grade_report_student(role, email_id)

            elif sub_choice == "2":
                grades_instance = Grades()
                grades_instance.grade_report_professor(role, email_id)
                
            elif sub_choice == "3":
                grades_instance = Grades()
                grades_instance.grade_report_course(role, email_id)

            elif sub_choice == "4":
                continue # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "10":
            break # Return to main menu

        else:
            print("Invalid choice, please enter again.")

def professor_menu(role, email_id):
    while True:
        print("\nProfessor Menu:")
        print("1. Display Student Records")
        print("2. Display Professor Records")
        print("3. Display Course Records")
        print("4. Display Grades Records")
        print("5. Modify My Details") 
        print("6. Add/Delete/Modify Course")
        print("7. Add/Delete/Modify Grades")
        print("8. Generate Grade Report") 
        print("9. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n Display Student Records Menu:")
            print("1. Display the details of all students in my courses")
            print("2. Display all students details")
            print("3. Display chosen student details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                sort_by = input("Enter the sort by (student_id, first_name, last_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                student_instance = Student()
                student_instance.display_professor_student_records(email_id, sort_by, reverse)

            elif sub_choice == "2":
                sort_by = input("Enter the sort by (student_id, first_name, last_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                student_instance = Student()
                student_instance.display_all_students_records(sort_by, reverse)

            elif sub_choice == "3":
                students[list(students.keys())[0]].display_chosen_student_records()

            elif sub_choice == "4":
                break # Return to previous menu

            else:
                print("Invalid choice, please enter again.")

        elif choice == "2":
            print("\n Display Professor Records Menu:")
            print("1. Display my details")
            print("2. Display all professors details")
            print("3. Display chosen professor details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                professor_instance = Professor()
                professor_instance.display_professor_himself(email_id)

            elif sub_choice == "2":
                sort_by = input("Enter the sort by (professor_id, name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                professor_instance = Professor()
                professor_instance.display_all_professors_records(sort_by, reverse)

            elif sub_choice == "3":
                professors[list(professors.keys())[0]].display_chosen_professor_records()

            elif sub_choice == "4":
                break   # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "3":
            print("\n Display Course Records Menu:")
            print("1. Display the details of all courses which I teach")
            print("2. Display all courses details")
            print("3. Display chosen course details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                course_instance = Course()
                course_instance.display_course_taught_by_professor_records(email_id)

            elif sub_choice == "2":
                sort_by = input("Enter the sort by (course_id, course_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                course_instance = Course()
                course_instance.display_all_courses_records(sort_by, reverse)

            elif sub_choice == "3":
                courses[list(courses.keys())[0]].display_chosen_course_records()

            elif sub_choice == "4":
                break  # Return to previous menu

            else:  
                print("Invalid choice, please enter again.")
        
        elif choice == "4":
            print("\n Display Grades Records Menu:")
            print("1. Display the grades of all courses which I teach")
            print("2. Display the grades of chosen course which I teach")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()
            
            if sub_choice == "1":
                sort_by = input("Enter the sort by (student_id, grades, marks): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                grades_instance = Grades()
                grades_instance.display_professor_grades(email_id, sort_by, reverse)

            elif sub_choice == "2":
                course_id = input("Enter the course ID: ").strip()
                sort_by = input("Enter the sort by (student_id, grades, marks): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                grades_instance = Grades()
                grades_instance.display_professor_chosen_grades(email_id, course_id, sort_by, reverse)
        
            elif sub_choice == "3":
                break # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "5":
            professor_instance = Professor()
            professor_instance.modify_professor_details(email_id)

        elif choice == "6":
            print("\n Add/Delete/Modify Course Menu:")
            print("1. Add new course")
            print("2. Delete course")
            print("3. Modify course details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                course_instance = Course()
                course_instance.add_new_course_professor(email_id)

            elif sub_choice == "2":
                course_instance = Course()
                course_instance.delete_course(role, email_id)

            elif sub_choice == "3":
                course_instance = Course()
                course_instance.modify_course(role, email_id)

            elif sub_choice == "4":
                break
            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "7":
            print("\n Add/Delete/Modify Grades Menu:")
            print("1. Add new grade")
            print("2. Delete grade")
            print("3. Modify grade details")
            print("4. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice == "1":
                grades_instance = Grades()
                grades_instance.add_new_grade(role, email_id)

            elif sub_choice == "2":
                grades_instance = Grades()
                grades_instance.delete_grade(role, email_id)

            elif sub_choice == "3":
                grades_instance = Grades()
                grades_instance.modify_grade(role, email_id)

            elif sub_choice == "4":
                break # Return to previous menu

            else:
                print("Invalid choice, please enter again.")
        
        elif choice == "8":
            print("\n Generate Grade Report Menu:")
            print("1. Generate grade report for all my courses")
            print("2. Generate grade report for a specific course I taught")
            print("3. Return to previous menu")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                grades_instance = Grades()
                grades_instance.grade_report_professor(role, email_id)

            elif sub_choice == "2":
                grades_instance = Grades()
                grades_instance.grade_report_course(role, email_id)
        
        elif choice == "9":
            break

        else:
            print("Invalid choice, please enter again.")

def student_menu(role, email_id):
    while True:
        print("\nStudent Menu:")
        print("1. Display My Records")
        print("2. Modify My Details")
        print("3. Check My Grades")
        print("4. Check My Marks")
        print("5. Generate My Grade Report")
        print("6. Discover Courses") 
        print("7. Discover Professors") 
        print("8. Return to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_instance = Student()
            student_instance.display_student_himself_records(email_id)

        elif choice == "2":
            student_instance = Student()
            student_instance.modify_student_records(role, email_id)

        elif choice == "3":
            student_instance = Student()
            student_instance.check_my_grades(email_id)

        elif choice == "4":
            student_instance = Student()
            student_instance.check_my_marks(email_id)

        elif choice == "5":
            grades_instance = Grades()
            grades_instance.grade_report_student(role, email_id)

        elif choice == "6":
            print("\n Discover Courses Menu:")
            print("1. Display all courses")
            print("2. Display chosen course details")
            print("3. Return to previous menu")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                sort_by = input("Enter the sort by (course_id, course_name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                course_instance = Course()
                course_instance.display_all_courses_records(sort_by, reverse)

            elif choice == "2":
                courses[list(courses.keys())[0]].display_chosen_course_records()

            elif choice == "3":
                break

            else:
                print("Invalid choice, please enter again.")

        elif choice == "7":
            print("\n Discover Professors Menu:")
            print("1. Display all professors")
            print("2. Display chosen professor details")
            print("3. Return to previous menu")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                sort_by = input("Enter the sort by (professor_id, name): ").strip()
                reverse_input  = input("Enter True, sort in descending order, enter False, sort in ascending order): ").strip().lower()
                if reverse_input == "true":
                    reverse = True
                elif reverse_input == "false":
                    reverse = False
                else:
                    print("Invalid input for reverse. Defaulting to False.")
                    reverse = False
                professor_instance = Professor()
                professor_instance.display_all_professors_records(sort_by, reverse)

            elif choice == "2":
                professors[list(professors.keys())[0]].display_chosen_professor_records()

            elif choice == "3":
                break # Return to previous menu

            else:
                print("Invalid choice, please enter again.")

        elif choice == "8":
            break # Return to main menu

        else:
            print("Invalid choice, please enter again.")


if __name__ == "__main__":
    main_menu()