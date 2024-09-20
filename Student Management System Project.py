class Student:
    student_dictionary={}
    school_name="Vinay's School"
    
    def __init__(self):
        self.roll_no=input("\n\tEnter the Student Roll Number: ")
        self.name=input("\tEnter the Student Name: ")
        self.phone_number=input("\tEnter the Student Phone Number: ")
        self.address=input("\tEnter the Student Address: ")
        student_class=input("\tEnter the Student Class[Ex: 1 2 3 4 5 6 7 8 9 10]: ")
        
        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
            
        else:
            new_class=StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class]=new_class
            
        self.student_class=StudentClass.classes[student_class]
        print("\nStudent Added Successfully")
        self.getStudent()
        
    def getStudent(self):
        print("\n-----STUDENT DETAILS-----\n")
        print("\tRoll Number:",self.roll_no)
        print("\tName:",self.name)
        print("\tPhone Number:",self.phone_number)
        print("\tAddress:",self.address)
        print("\tClass:",self.student_class.name)
        print("\tSchoolName: Vinay's School")
    
    def updateStudent(self):
        print("\t\tselect option to update student details\n")
        print("\t\t\t 1)To Change Student Name")
        print("\t\t\t 2)To Change Student Phone Number")
        print("\t\t\t 3)To Change Student Address")
        print("\t\t\t 4)To Change Student Class\n")
        option=input("\t\tEnter any above given option: ")
        print()
        
        if option in ['1','2','3','4']:
            if option=='1':
                self.name=input("\t\t\tEnter the Student New Name: ")
                print("\n\t\tStudent Name Changed Successfully\n")
                
            elif option=='2':
                self.phone_number=input("\t\t\tEnter the Student New Phone Number: ")
                print("\n\t\tStudent Phone Number Changed Successfully")
                
            elif option=='3':
                self.address=input("\t\t\tEnter the Student New Address: ")
                print("\n\t\tStudent Address Changed Successfully\n")
                
            elif option=='4':
                new_class=input("\t\t\tEnter the Student New Class Name: ")
                self.student_class.studentList.remove(self)
                try:
                    self.student_class=StudentClass.classes[new_class]
                    self.student_class.studentList.append(self)
                except:
                    addClass=StudentClass(new_class)
                    self.student_class=addClass
                    addClass.studentList.append(self)
                    print("\n\t\tStudent Class Changed Successfully\n")
                
            self.getStudent()
        else:
            print("\n\t\t\tYou have Choosen wrong option")
            
    @classmethod
    def updateSchoolName(cls,new_school_name):
        cls.school_name=new_school_name
        
    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)

class StudentClass:
    classes={}
    
    def __init__(self,name):
        self.name=name
        StudentClass.classes[name]=self
        self.studentList=[]

def main():
    print(f"---Welcome To {Student.school_name}---\n")
    print("\t 1)To Get Student Details")
    print("\t 2)To Add New Student")
    print("\t 3)To Remove Student")
    print("\t 4)To Update Student Details")
    print("\t 5)To Update School Name")
    print("\t 6)To Get Number of Students in School")
    print("\t 7)To Get All Students Details")
    print("\t 8)To Get Any Class Student Details")
    
    option=input("\nEnter Any Above Option: ")
    print()
    
    if option=='1':
        roll_no=input("\tEnter the Roll Number of a Student: ")
        try:
            Student.student_dictionary[roll_no].getStudent()
        except:
            print("\t\tYou Have Entered the wrong roll number")
            
    elif option=='2':
        new_student=Student()
        Student.student_dictionary[new_student.roll_no]=new_student
        
    elif option=='3':
        roll_no=input("\tEnter the Roll Number of a Student: ")
        try:
            student=Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print('\t\t','''''',roll_no,'''''','Student Deleted Successfully')
        except:
            print("\t\tNo Student there to Delete")
        
    elif option=='4':
        roll_no=input("\tEnter the Roll Number of a Student: ")
        print()
        try:
            Student.student_dictionary[roll_no].updateStudent()
        except:
            print("\n\t\tYou have entered the wrong roll number")
            
    elif option=='5':
        new_school_name=input("\tEnter the New School Name")
        Student.updateSchoolName(new_school_name)
        print("School Name Changed Successfully")
        
    elif option=='6':
        print("Total Number of Students in School:",Student.getTotalStudentCount())
        
    elif option=='7':
        if Student.student_dictionary:
            print("Total Number of Students in School:",Student.getTotalStudentCount())
            print("\nTotal Student List with Details\n")
            for sNo,student in enumerate(Student.student_dictionary.values()):
                print("Student-",sNo+1)
                student.getStudent()
                print()
        else:
            print("\tNo Students Are There")
            
    elif option=='8':
        try:
            students=StudentClass.classes[input("\tEnter the Class Name: ")]
            print("\nStudents of Class-",students.name)
            print(f"Total Number of Students In Class {students.name}:{len(students.studentList)}")
            print()
            for sNo,student in enumerate(students.studentList):
                    print("Student-",sNo+1)
                    student.getStudent()
                    print()
        except:
            print("\nYou Entered wrong class name or no students are there")

if __name__ == '__main__':
    option='y'
    while option=='y':
        main()
        option=input("\nDo you want to Continue [y/n?]: ")
        print()