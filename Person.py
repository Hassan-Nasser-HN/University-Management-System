from dataclasses import dataclass

@dataclass
class Name:
    first: str
    sec: str
    third: str


class Person:
    def __init__(self, name, age, person_id):
        self.__name = name
        self.__age = age
        self.__person_id = person_id

    def Display_info(self):
        print(f"Name: {self.get_name()}\n"
              f"Age: {self.get_age()}\n"
              f"ID: {self.get_person_id()}\n")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_person_id(self):
        return self.__person_id

    def set_name(self, Name):
      if Name.frist.isalpha() and Name.sec.isalpha() and Name.thir.isalpha():
        self.__name = name
      else:
        print("Name must contain letters only")

    def set_age(self, age):
      if age.isdigit() and isinstance(age, int) and  0<= age <= 150 :
        self.__age = age
      else:
        print("The age is not valid")

    def set_person_id(self, person_id):

     if  len(person_id) == 14:
        self.__person_id = person_id
     else:
        print("Person ID must be 14 characters")
class Student(Person):
    def __init__(self, name, age, person_id, academic_id,
                 department, level=1, gpa=0.0,cgpa=0.0, passed_hours=0,
                 all_courses_passed = {},gpa_semesters=[],hours_semesters=[]):
        super().__init__(name, age, person_id)
        self.__poswered
        self.__email
        self.__academic_id = academic_id
        self.__department = department
        self.__level = level
        self.__gpa = gpa
        self.__cgpa=cgpa
        self.__course_semester = []
        self.__all_courses_passed = all_courses_passed
        self.__max_hours = 17
        self.__passed_hours = passed_hours
        self.__gpa_semesters=gpa_semesters
        self.__hours_semesters=hours_semesters

    def Display_info(self):
        super().Display_info()
        print(f"Academic ID: {self.get_academic_id()}\n"
              f"Department: {self.get_department()}\n"
              f"Level: {self.get_level()}\n"
              f"GPA: {self.get_gpa()}\n"
              f"Passed Hours: {self.get_passed_hours()}\n")

    def get_academic_id(self):
        return self.__academic_id

    def get_department(self):
        return self.__department

    def get_level(self):
        return self.__level

    def get_gpa(self):
        return self.__gpa

    def get_cgpa(self):
      return self.__cgpa

    def get_course_semester(self):
        return self.__course_semester

    def get_all_courses_passed(self):
        return self.__all_courses_passed

    def get_max_hours(self):
        return self.__max_hours

    def get_passed_hours(self):
        return self.__passed_hours

    def set_academic_id(self, academic_id):
      if academic_id.len()==14:
        self.__academic_id = academic_id
      else:
        print("Academic ID must be 14 characters")

    def set_department(self, department):
       if self.get_cgpa() >= department.get_min_gpa():
        self.__department = department
       else:
        print("CGPA is not enough for this department")

    def set_level(self, level):
       if 1 <= level <= 5:
        self.__level = level
       else:
        print("Level must be between 1 and 5")

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
          print("GPA must be between 0.0 and 4.0")

    def set_cgpa(self, cgpa):
        if 0.0 <= cgpa <= 4.0:
            self.__cgpa = cgpa
        else:
          print("CGPA must be between 0.0 and 4.0")

    def set_course_semester(self, course):
     if course in self.department.get_courses():
         self.__course_semester.append(course)
     else:
        print("Course is not available in this department")

    def set_max_hours(self, max_hours):
        if max_hours in {12, 17, 21}:
            self.__max_hours = max_hours
        else:
            print("Not allowed")

    def set_passed_hours(self, hours):
     if 0 <= hours <= self.get_max_hours():
        self.__passed_hours = hours
     else:
         print("Invalid passed hours")

