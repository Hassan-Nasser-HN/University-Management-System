class Enrollment:
    def __init__(self, student):
        self.__student = student
        self.__total_hours = 0

    def add_course(self, course):
        if course in self.__student.get_course_semester():
            print("Course is already registered.")
            return
        prerequisites = course.get_prerequisites()

        for prerequisite in prerequisites:
            if prerequisite not in self.__student.get_all_courses_passed():
                print("You cannot register this course.")
                print(f"You must pass {prerequisite} first.")
                return

        if self.__total_hours + course.get_credit_hours() > self.__student.get_max_hours():
            print("Not enough credit hours.")
            return
        self.__student.set_course_semester(course)
        self.__total_hours += course.get_credit_hours()

        print("Course added successfully.")
        print(f"Remaining hours: {self.__student.get_max_hours() - self.__total_hours}")

    def drop_course(self, course):
        if course not in self.__student.get_course_semester():
            print("Course is not registered.")
            return
        self.__student.get_course_semester().remove(course)
        self.__total_hours -= course.get_credit_hours()

        print("Course dropped successfully.")
        print(f"Remaining hours: {self.__student.get_max_hours() - self.__total_hours}")

    def display_courses(self):
        courses = self.__student.get_course_semester()

        if not courses:
            print("No courses registered.")
            return

        print("Registered Courses:")
        for course in courses:
            print(f"Code: {course.get_code()}\n"
                  f"Name: {course.get_title()}\n"
                  f"Hours: {course.get_credit_hours()}\n")

        print(f"Total hours: {self.__total_hours}")

class Grade:
    def __init__(self, student, course):
        self.__student = student
        self.__course = course
        self.__mark = 0

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            print("Invalid mark. Mark must be between 0 and 100.")
            return

        self.__mark = mark
        letter_grade = self.get_letter_grade()
        self.__student.get_all_courses_passed()[self.__course.get_code()] = letter_grade

        if letter_grade != "F":
            self.__student.set_passed_hours(self.__student.get_passed_hours() + self.__course.get_credit_hours())

    def get_letter_grade(self):
        if self.__mark >= 90:
            return "A"
        elif self.__mark >= 80:
            return "B"
        elif self.__mark >= 70:
            return "C"
        elif self.__mark >= 60:
            return "D"
        else:
            return "F"

    def calculate_gpa(self):
        courses = self.__student.get_course_semester()

        if not courses:
            self.__student.set_gpa(0.0)
            return 0.0

        total_points = 0.0
        total_hours = 0

        grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

        for course in courses:
            code = course.get_code()
            if code in self.__student.get_all_courses_passed():
                letter_grade = self.__student.get_all_courses_passed()[code]
                points = grade_points[letter_grade]
                hours = course.get_credit_hours()
                total_points += points * hours
                total_hours += hours

        if total_hours == 0:
            gpa = 0.0
        else:
            gpa = total_points / total_hours
            self.__student.set_gpa(gpa)
        return gpa

    def get_mark(self):
        return self.__mark
