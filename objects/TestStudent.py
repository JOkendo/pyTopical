from Student import Student

def main():
    done = False
    while not done:
        ans = input("Enter 'y' to continue and 'n' to quit: ")
        if ans != 'n':
            '''name = input("Student's Name: ")
            gender = input("Gender: ")
            department = input("Department: ")
            acadYr = int(input("Academic Year: "))'''
            student = Student(name,gender,department,acadYr)
            
            student.setName("Jack Omondi")
            student.setGender("M")
            student.setDepartment("Computer Science")
            student.setAcadYr(4)
            student.level()
            student.display()
        else:
            done = True
main()