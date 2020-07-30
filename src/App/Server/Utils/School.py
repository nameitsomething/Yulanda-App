from .Student import Student
from .Course import Course
import csv
from datetime import datetime

class School:

    def __init__(self):
        self.students = []
        self.courses = []
        self.student_numbers =

    def add_student(self, student: Student):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return False

            student.set_student_number(self.student_numbers)
            self.student_numbers += 1

            self.students.append(student)
            return True

        return False

    def remove_student(self, student: Student = None, name: str = None, number: int = None):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    for c in self.courses:
                        c.remove_student(s) # from all courses

                    self.students.remove(s) # from the school
                    return True

        if name != None:
            for s in self.students:
                if s.name == name:
                    for c in self.courses:
                        c.remove_student(s)

                    self.students.remove(s)
                    return True

        if number != None:
            for s in self.students:
                if s.student_number == number:
                    for c in self.courses:
                        c.remove_student(s)

                    self.students.remove(s)
                    return True

        return False

    def add_student_to_course(self, student: Student = None, student_name: str = None, student_number: int = None,
                              course: Course = None, course_name : str = None, course_number : int = None,
                              course_section : int = None):
        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        if student_name != None:
            for s in self.students:
                if s.name == student_name:
                    temp_student = s

        if student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if temp_student == None:
            return False

        if course != None:
            for c in self.courses:
                if c.number == course.number and c.section == course.section:
                    c.add_student(temp_student)
                    return True

        if course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.add_student(temp_student)
                    return True

        if course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.add_student(temp_student)
                    return True

        return False

    def remove_student_to_course(self, student: Student = None, student_name: str = None, student_number: int = None,
                              course: Course = None, course_name: str = None, course_number: int = None,
                              course_section: int = None):

        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        if student_name != None:
            for s in self.students:
                if s.name == student_name:
                    temp_student = s

        if student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    temp_student = s

        if temp_student == None:
            return False

        if course != None:
            for c in self.courses:
                if c.number == course.number and c.section == course.section:
                    c.remove_student(temp_student)
                    return True
            return False

        if course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.remove_student(temp_student)
                    return True
            return False

        if course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.remove_student(temp_student)
                    return True
            return False
        return False

    def add_course(self, course: Course):
        if course != None:
            for c in self.courses:
                if course.section == c.section and (course.name == c.name or course.number == c.number):
                    return False
            self.courses.append(course)
            return True
        return False

    def remove_course(self, course: Course = None, course_name: str = None, course_number: int = None,
                      course_section: int = None):
        if course != None:
            for c in self.courses:
                if course.section == c.section and (course.name == c.name or course.number == c.number):
                    self.courses.remove(c)
                    return True

        if course_section != None and (course_name != None or course_number != None):
            for c in self.courses:
                if c.section == course_section and (c.name == course_name or c.number == course_number):
                    self.courses.remove(c)
                    return True

        return False

    def get_course(self, course_name: str = None, course_number: int = None, course_section: int = None):
        if course_name != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    return c
        if course_number != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    return c

    def get_student(self, student_name: str = None, student_number: int = None):
        if student_name != None:
            for s in self.students:
                if s.name == student_name:
                    return s
        if student_number != None:
            for s in self.students:
                if s.student_number == student_number:
                    return s

    def write(self):
        with open('students.csv', "w") as file:
            for s in self.students:
                file.write(s.format_csv())

        with open('classes.csv', "w") as file:
            for c in self.courses:
                file.write(c.format_csv())

    def read(self):
        with open('students.csv', "r", newline='') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                self.student.append(Student(str(row[0]), int(row[1]), int(row[2]), bool(row[3])).set_student_number(int(row[4])))

        with open('classes.csv', "r", newline='') as file:
            reader = csv.reader(file, delimiter=',')

            for row in reader:
                times = []
                students = []
                for i in range(0, int(row[4])):
                    times.append(datetime.datetime.strptime(row[6+i], '%Y-%m-%d %H:%M:%S.%f'))

                for i in range(0, int(row[5])):
                    students.append(int(row[ int(row[4] + i + 6)]))


                temp = Course(str(row[0]), int(row[1]), int(row[2]), str(row[3]))

                for t in times:
                    temp.add_time(t)

                for s in students:
                    for stu in self.students:
                        if s == stu.student_number:
                            temp.add_student(stu)
                            break

