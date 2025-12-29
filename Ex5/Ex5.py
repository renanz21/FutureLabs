class Student: #Student class
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Teacher: #Teacher class
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = []

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Hteacher:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

students = {}
teachers = {}
hteachers = {}

def create_student():
    first = input("Enter students' first name: ").strip()
    last = input("Enter students' last name: ").strip()
    class_name = input("Enter students' class name: ").strip()

    st = Student(first, last, class_name)
    students[st.full_name()] = st
    print("Student created")
    print(st)

def create_teacher():
    first = input("Enter teachers' first name: ").strip()
    last = input("Enter teacers' last name: ").strip()
    subject = input("Enter teachers' subject name: ").strip()

    tc = Teacher(first, last, subject)

    print("Enter class names, enter blank space to stop")
    while True:
        class_name = input("Class name: ").strip()
        if class_name == "":
            break
        tc.classes.append(class_name)

    teachers[tc.full_name()] = tc
    print("Teacher created")
    print(tc)

def create_hteacher():
    first = input("Enter homeroom teachers' first name: ").strip()
    last = input("Enter homeroom teachers' last name: ").strip()
    class_name = input("Enter homeroom teachers' class name: ").strip()

    htc = Hteacher(first, last, class_name)
    hteachers[htc.full_name()] = htc
    print("Homeroom teacher created")
    print(htc)

def create_user():
    print("Types of users: \n-Student\n-Teacher\n-Homeroom teacher\nEnd")

    while True:
        choice = input("Choose an user to create or type end to 'End' to exit")

        if choice == "student":
            create_student()

        elif choice == "teacher":
            create_teacher()

        elif choice == "homeroom teacher":
            create_hteacher()

        elif choice == "end":
            return

        else:
            print("Invalid choice")



def manage_user():

    print("Manageable sections: Class, Student, Teacher, Homeroom teacher, End")

    while True:
        choice = input("Manage option: ").strip().lower()

        if choice == "class":
            manage_class()

        if choice == "student":
        if choice == "teacher":
        if choice == "homeroom teacher":
        if choice == "end":
            return

        else:
            print("Invalid choice")

def main():

    print("Options: create, manage, end")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "create":
            create_user()

        elif command == "manage":
            manage_user()

        elif command == "end":
            print("Program halted")

        else:
            print("Invalid command")