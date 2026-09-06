class UniversitySystem:
    def __init__(self):
        self.__students = []
        self.__instructors = []
        self.__courses = []
        self.__departments = []
        self.__graduated_students = []
        self.__level_hours = {1: 32, 2: 64, 3: 96, 4: 132}
        self.__enrollments = {}

    def add_student(self, student):
        for s in self.__students:
            if s.get_person_id() == student.get_person_id():
                print("Student already exists.")
                return
        self.__students.append(student)
        print("Student added successfully.")

    def add_instructor(self, instructor):
        for i in self.__instructors:
            if i.get_person_id() == instructor.get_person_id():
                print("Instructor already exists.")
                return
        self.__instructors.append(instructor)
        print("Instructor added successfully.")

    def add_course(self, course):
        for c in self.__courses:
            if c.get_code() == course.get_code():
                print("Course already exists.")
                return
        self.__courses.append(course)
        print("Course added successfully.")

    def add_department(self, department):
        for d in self.__departments:
            if d.get_name_department() == department.get_name_department():
                print("Department already exists.")
                return
        self.__departments.append(department)
        print("Department added successfully.")

    def search_student(self, person_id):
        for student in self.__students:
            if student.get_person_id() == person_id:
                return student
        print("Student not found.")
        return None

    def search_course(self, code):
        for course in self.__courses:
            if course.get_code() == code:
                return course
        print("Course not found.")
        return None

    def display_student(self, person_id):
        student = self.search_student(person_id)
        if student is not None:
            student.Display_info()

    def display_department(self, name_department):
        for department in self.__departments:
            if department.get_name_department() == name_department:
                department.Display_info()
                return
        print("Department not found.")

    def update_student(self, person_id, name=None, age=None, academic_id=None, department=None, level=None):
        student = self.search_student(person_id)
        if student is None:
            return
        if name is not None:
            student.set_name(name)
        if age is not None:
            student.set_age(age)
        if academic_id is not None:
            student.set_academic_id(academic_id)
        if department is not None:
            student.set_department(department)
        if level is not None:
            student.set_level(level)
        print("Student updated successfully.")

    def remove_student(self, person_id):
        student = self.search_student(person_id)
        if student is None:
            return
        self.__students.remove(student)
        print("Student removed successfully.")

    def enroll_student(self, student_id, course_code):
        student = self.search_student(student_id)
        if student is None:
            return
        course = self.search_course(course_code)
        if course is None:
            return
        enrollment = self.__enrollments.get(student_id)
        if enrollment is None:
            enrollment = Enrollment(student)
            self.__enrollments[student_id] = enrollment
        enrollment.add_course(course)

    def display_student_courses(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            return
        enrollment = self.__enrollments.get(student_id)
        if enrollment is None:
            print("No courses registered.")
            return
        enrollment.display_courses()

    def add_grade(self, student_id, course_code, mark):
        student = self.search_student(student_id)
        if student is None:
            return
        course = self.search_course(course_code)
        if course is None:
            return
        grade = Grade(student, course)
        grade.add_mark(mark)

    def assign_instructor(self, instructor_id, course_code):
        instructor = None
        for i in self.__instructors:
            if i.get_instructor_id() == instructor_id:
                instructor = i
                break
        if instructor is None:
            print("Instructor not found.")
            return
        course = self.search_course(course_code)
        if course is None:
            return
        course.set_instructor(instructor)
        print(f"Instructor {instructor.get_name()} assigned to {course.get_title()}.")

    def end_semester(self):
        for student in self.__students[:]:
            grade = Grade(student, None)
            grade.calculate_gpa()

            current_level = student.get_level()
            if student.get_passed_hours() >= self.__level_hours[4]:
                print(f"{student.get_name()} has graduated.")
                self.__students.remove(student)
                self.__graduated_students.append(student)
                continue

            if current_level < 4 and student.get_passed_hours() >= self.__level_hours[current_level]:
                student.set_level(current_level + 1)
                print(f"{student.get_name()} moved to level {student.get_level()}.")

            student.get_course_semester().clear()
            self.__enrollments[student.get_person_id()] = Enrollment(student)

    def get_graduated_students(self):
        return self.__graduated_students
