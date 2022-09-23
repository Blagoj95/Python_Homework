class Person:
    def __init__(self,fname,lname,email,mobnumb):
         self.firstname = str(fname)
         self.lastname = str(lname)
         self.email = str(email)
         self.mobilenumber = int(mobnumb)
    
    def info_person(self):
         print(f"Person:\n First name: {self.firstname}\n Last name: {self.lastname}\n "
             f"Email:{self.email}\n Mobile:+ {self.mobilenumber}\n")
