from person import Person
from email_validator import validate_email, EmailSyntaxError

class Student(Person):
    def __init__(self, fname, lname, email, mobnumb):
        super().__init__(fname, lname, email, mobnumb)
       
        
    def info(self):
        print(f"Is a Student of the following courses and has grades")
        courses =  {
            "Git":"7",
            "Python":8,
            "AWS":10,
            "Docker":3,
            "Linux":4
            }
        count = 1 
        for course in courses:
            print(f"{count}.{course}:{courses[course]}")
            count+=1


name = input("Enter your name: ")
surname = input("Enter your surname: ")
email = input("Enter your email: ")
email = input("Invalide email address, Enter valid email addres: ")
try:
    email = validate_email(email).email
except EmailSyntaxError as e:
    print(str(e))
number = input("Enter your phone number: ")


x = Student(name,surname,email,number)
x.info_person()
x.info()
