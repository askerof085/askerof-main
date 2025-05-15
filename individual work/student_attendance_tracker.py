import json
import os
from datetime import datetime
import time


class StudentAttendanceTracker:
    def __init__(self):
        self.students = {}
        self.filename = "attendance_data.json"
        self.load_data()

    def welcome_screen(self):
        print("\n" + "="*50)
        print("Welcome to Student Attendance Tracker")
        print("Created by: Əskərov Yusif Bəhruz")
        print("="*50 + "\n")
        time.sleep(2)
        print("Loading data...")
        time.sleep(2)
        print("Data loaded successfully!")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Add new student")
            print("2. View all students")
            print("3. Search student")
            print("4. Update student record")
            print("5. Delete student record")
            print("6. View attendance statistics")
            print("7. Sort students")
            print("8. Help")
            print("9. Save and Exit")
            
            try:
                choice = int(input("\nEnter your choice (1-9): "))
                if choice == 1:
                    self.add_student()
                    time.sleep(2)
                elif choice == 2:
                    self.view_all_students()
                    time.sleep(3)
                elif choice == 3:
                    self.search_student()
                    time.sleep(2)
                elif choice == 4:
                    self.update_student()
                    time.sleep(2)
                elif choice == 5:
                    self.delete_student()
                    time.sleep(2)
                elif choice == 6:
                    self.view_statistics()
                    time.sleep(2)
                elif choice == 7:
                    self.sort_students()
                    time.sleep(2)
                elif choice == 8:
                    self.show_help()
                    time.sleep(2)
                    print("Returning to main menu...")
                    time.sleep(1)
                elif choice == 9:
                    print("Saving data...")
                    self.save_data()
                    print("Thank you for using Student Attendance Tracker!")
                    print("Goodbye!")
                    time.sleep(2)
                    break
                else:
                    print("Invalid choice! Please try again.")
            except ValueError:
                print("Please enter a valid number!")

    def add_student(self):
        try:
            student_id = input("Enter student ID: ")
            if student_id in self.students:
                print("Student ID already exists!")
                return
            
            name = input("Enter student name: ")
            attendance = int(input("Enter attendance count: "))
            
            self.students[student_id] = {
                "name": name,
                "attendance": attendance,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("Student added successfully!")
        except ValueError:
            print("Invalid input! Please enter correct data types.")
        

    def view_all_students(self):
        if not self.students:
            print("No students in the database!")
            return
        
        print("\nStudent Records:")
        print("-" * 50)
        for student_id, data in self.students.items():
            print(f"ID: {student_id}")
            print(f"Name: {data['name']}")
            print(f"Attendance: {data['attendance']}")
            print(f"Last Updated: {data['last_updated']}")
            print("-" * 50)

    def search_student(self):
        search_id = input("Enter student ID to search: ")
        if search_id in self.students:
            data = self.students[search_id]
            print("\nStudent Found:")
            print(f"ID: {search_id}")
            print(f"Name: {data['name']}")
            print(f"Attendance: {data['attendance']}")
            print(f"Last Updated: {data['last_updated']}")
        else:
            print("Student not found!")

    def update_student(self):
        student_id = input("Enter student ID to update: ")
        if student_id in self.students:
            try:
                name = input("Enter new name (press Enter to keep current): ")
                attendance = input("Enter new attendance count (press Enter to keep current): ")
                
                if name:
                    self.students[student_id]['name'] = name
                if attendance:
                    self.students[student_id]['attendance'] = int(attendance)
                
                self.students[student_id]['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Student record updated successfully!")
            except ValueError:
                print("Invalid input! Please enter correct data types.")
        else:
            print("Student not found!")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student record deleted successfully!")
        else:
            print("Student not found!")

    def view_statistics(self):
        if not self.students:
            print("No students in the database!")
            return
        
        total_students = len(self.students)
        total_attendance = sum(data['attendance'] for data in self.students.values())
        avg_attendance = total_attendance / total_students
        
        print("\nAttendance Statistics:")
        print(f"Total Students: {total_students}")
        print(f"Total Attendance: {total_attendance}")
        print(f"Average Attendance: {avg_attendance:.2f}")

    def sort_students(self):
        if not self.students:
            print("No students in the database!")
            return
        
        print("\nSort by:")
        print("1. ID")
        print("2. Name")
        print("3. Attendance")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                sorted_students = dict(sorted(self.students.items()))
            elif choice == 2:
                sorted_students = dict(sorted(self.students.items(), key=lambda x: x[1]['name']))
            elif choice == 3:
                sorted_students = dict(sorted(self.students.items(), key=lambda x: x[1]['attendance']))
            else:
                print("Invalid choice!")
                return
            
            print("\nSorted Student Records:")
            for student_id, data in sorted_students.items():
                print(f"ID: {student_id}, Name: {data['name']}, Attendance: {data['attendance']}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    def show_help(self):
        print("\nHelp Guide:")
        print("1. Add new student: Enter student details to add a new record")
        print("2. View all students: Display all student records")
        print("3. Search student: Find a specific student by ID")
        print("4. Update student: Modify existing student records")
        print("5. Delete student: Remove a student record")
        print("6. View statistics: See attendance statistics")
        print("7. Sort students: Sort records by ID, name, or attendance")
        print("8. Help: Show this help guide")
        print("9. Save and Exit: Save data and exit the program")
    def save_data(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.students, f, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.students = json.load(f)
                print("Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.students = {}

def main():
    tracker = StudentAttendanceTracker()
    tracker.welcome_screen()
    tracker.main_menu()

if __name__ == "__main__":
    main()
# Hər dəfə menyudan nə isə seçsəniz, 2 saniyə time sleep qoyulub ki, istifadəçi rahat oxuya bilsin.
# Həmçinin, hər dəfə menyudan çıxanda məlumatları saxlayır.
