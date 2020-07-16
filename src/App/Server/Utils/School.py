from .Student import Student
from .Course import Course
import csv


class School:

    def __init__(self):
        self.students = []
        self.courses = []
        self.student_numbers = 0

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

        elif name != None:
            for s in self.students:
                if s.name == name:
                    for c in self.courses:
                        c.remove_student(s)

                    self.students.remove(s)
                    return True

        elif number != None:
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

        elif student_name != None:
            for s in self.students:
                if s.name == student_name:
                    temp_student = s

        elif student_number != None:
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
            return False

        elif course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.add_student(temp_student)
                    return True
            return False

        elif course_name != None and course_section != None:
            for c in self.courses:
                if c.name == course_name and c.section == course_section:
                    c.add_student(temp_student)
                    return True
            return False

        return False

    def remove_student_to_course(self, student: Student = None, student_name: str = None, student_number: int = None,
                              course: Course = None, course_name: str = None, course_number: int = None,
                              course_section: int = None):

        temp_student = None

        if student != None:
            for s in self.students:
                if s.name == student.name:
                    temp_student = s

        elif student_name != None:
            for s in self.students:
                if s.name == student_name:
                    temp_student = s

        elif student_number != None:
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

        elif course_number != None and course_section != None:
            for c in self.courses:
                if c.number == course_number and c.section == course_section:
                    c.remove_student(temp_student)
                    return True
            return False

        elif course_name != None and course_section != None:
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
            return False
        elif course_section != None and (course_name != None or course_number != None):
            for c in self.courses:
                if c.section == course_section and (c.name == course_name or c.number == course_number):
                    self.courses.remove(c)
                    return True
            return False
        return False

    def write(self):
        pass

    def read(self):
        pass