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
        print(f"Class {class_name} added, type blank to stop adding")

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
    print("\nTypes of users: \n-Student\n-Teacher\n-Homeroom teacher")

    while True:
        choice = input("Choose an user to create or type end to 'End' to exit")

        if choice == "student":
            create_student()
            print("\nTypes of users: \n-Student\n-Teacher\n-Homeroom teacher")

        elif choice == "teacher":
            create_teacher()
            print("\nTypes of users: \n-Student\n-Teacher\n-Homeroom teacher")

        elif choice == "homeroom teacher":
            create_hteacher()
            print("\nTypes of users: \n-Student\n-Teacher\n-Homeroom teacher")

        elif choice == "end":
            return

        else:
            print("Invalid choice")

def manage_class():
    class_name = input("Enter class name: ").strip()

    print(f"Students in {class_name}:")
    has_students = False
    for st in students.values():
        if st.class_name == class_name:
            print("-", st.full_name())
            print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")
            has_students = True

    if not has_students:
        print("No students found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

    print("Homeroom teacher:")
    found = False
    for ht in hteachers.values():
        if ht.class_name == class_name:
            print("-", ht.full_name())
            print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")
            found = True

    if not found:
        print("No homeroom teachers found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

def manage_students():
    first = input("Enter students' first name: ").strip()
    last = input("Enter students' last name: ").strip()
    full = f"{first} {last}"

    if full not in students:
        print("Student not found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")
        return

    st = students[full]
    print(f"Students attends class in: {st.class_name}:")
    print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

    print("Teachers: ")
    found = False
    for tc in teachers.values():
        if st.class_name in tc.classes:
            print("-", tc.full_name())
            found = True
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

    if not found:
        print("No teachers found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

def manage_teacher():
    first = input("Enter teachers' first name: ").strip()
    last = input("Enter teachers' last name: ").strip()
    full = f"{first} {last}"

    if full not in teachers:
        print("Teacher not found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")
        return

    print("Classes taught:")
    for c in teachers[full].classes:
        print("-", c)
    print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

def manage_hteacher():
    first = input("Enter homeroom teachers' first name: ").strip()
    last = input("Enter homeroom teachers' last name: ").strip()
    full = f"{first} {last}"

    if full not in hteachers:
        print("Homeroom teacher not found")
        print("Manageable sections: Class, Student, Teacher, Homeroom teacher, End")
        return

    class_name = hteachers[full].class_name

    print(f"Students led in {class_name}:")
    found = False
    for st in students.values():
        if st.class_name == class_name:
            print("-", st.full_name())
            found = True
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

    if not found:
        print("No students found")
        print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

def manage_user():

    print("\nManageable sections: Class, Student, Teacher, Homeroom teacher, End")

    while True:
        choice = input("Manage option: ").strip().lower()

        if choice == "class":
            manage_class()

        if choice == "student":
            manage_students()

        if choice == "teacher":
            manage_teacher()

        if choice == "homeroom teacher":
            manage_hteacher()

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
            print("Options: create, manage, end")

        elif command == "manage":
            manage_user()
            print("Options: create, manage, end")

        elif command == "end":
            print("Program halted")
            break

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()