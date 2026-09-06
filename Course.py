class Course:
    def __init__(self, code, title, credit_hours, level, prerequisites=None):
        self.__code = code
        self.__title = title
        self.__credit_hours = credit_hours
        self.__level = level
        self.__prerequisites = prerequisites if prerequisites is not None else []
        self.__instructor = None

    def Display_info(self):
        print(f"Code: {self.get_code()}\n"
              f"Title: {self.get_title()}\n"
              f"Credit Hours: {self.get_credit_hours()}\n"
              f"Level: {self.get_level()}\n"
              f"Prerequisites: {self.get_prerequisites()}\n")
        if self.get_instructor() is not None:
            print(f"Instructor: {self.get_instructor().get_name()}\n"
                  f"Instructor ID: {self.get_instructor().get_instructor_id()}\n")
        else:
            print("Instructor: Not assigned\n")

    def get_code(self):
        return self.__code

    def get_title(self):
        return self.__title

    def get_credit_hours(self):
        return self.__credit_hours

    def get_level(self):
        return self.__level

    def get_prerequisites(self):
        return self.__prerequisites

    def get_instructor(self):
        return self.__instructor

    def set_code(self, code):
        self.__code = code

    def set_title(self, title):
        self.__title = title

    def set_credit_hours(self, credit_hours):
        self.__credit_hours = credit_hours

    def set_level(self, level):
        self.__level = level

    def set_prerequisites(self, prerequisites):
        self.__prerequisites = prerequisites

    def set_instructor(self, instructor):
        self.__instructor = instructor

class Department:
    def __init__(self, name_department, max_students, min_gpa, courses=None):
        self.__name_department = name_department
        self.__max_students = max_students
        self.__min_gpa = min_gpa
        self.__courses = courses if courses is not None else []

    def Display_info(self):
        print(f"Department: {self.get_name_department()}\n"
              f"Minimum GPA: {self.get_min_gpa()}\n"
              f"Maximum Students: {self.get_max_students()}\n"
              f"Courses: {self.get_courses()}\n")

    def get_name_department(self):
        return self.__name_department

    def get_min_gpa(self):
        return self.__min_gpa

    def get_max_students(self):
        return self.__max_students

    def get_courses(self):
        return self.__courses

    def set_name_department(self, name_department):
        self.__name_department = name_department

    def set_min_gpa(self, min_gpa):
        self.__min_gpa = min_gpa

    def set_max_students(self, max_students):
        self.__max_students = max_students

    def set_courses(self, courses):
        self.__courses = courses
