class Student:
    def __init__(self, name, gender, department, acadYr = 1):
        self.__name = name
        self.__gender = gender
        self.__department = department
        self.__acadYr = acadYr
    
    def getName(self):
        return self.__name
    
    def getGender(self):
        if self.__gender == 'Male' or self.__gender == 'Female':
            return self.__gender

    def getDepartment(self):
        return self.__department

    def getAcadYr(self):
        return self.__acadYr
        
    def setName(self, name):
        self.__name = name
    
    def setGender(self, gender):
        if self.__gender == 'Male' or self.__gender == 'Female':
            self.__gender = gender

    def setDepartment(self, department):
        self.__department = department

    def setAcadYr(self, acadYr):
        self.__acadYr = acadYr

    def level(self):
        if self.getAcadYr() <= 6:
            return "Is Undergraduate"
        return "Graduate"

    def display(self):
        print("Name: ", self.getName(),"\nGender: ", self.getGender(), "\nDepartment: ", self.getDepartment(), "\nAcademic Year: ", self.getAcadYr())
        print("Level: ",self.level())