from .Student import Student
from datetime import datetime

class Course:

    def __init__(self, name: str, number: int, section: int, description: str):
        self.name = name
        self.number = number
        self.section = section
        self.description = description
        self.times = [] # times will be stored as timestamps relative to epoch, times will be displayed as ctime
        self.students = []

    def add_time(self, time: datetime):
        if time != None:
            for t in self.times:
                if t == time:
                    return False

            self.times.append(t)
            return True
        return False

    def remove_time(self, time: datetime):
        if time != None:
            for t in self.times:
                if t == time:
                    self.times.remove(t)
                    return True

        return False

    def add_student(self, student: Student):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return False

            self.students.append(student)
            return True
        return False

    def remove_student(self, student: Student = None, name: str = None, number: int = None):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    self.students.remove(s)
                    return True

        elif number != None:
            for s in self.students:
                if s.student_number == number:
                    self.students.remove(s)
                    return True

        elif name != None:
            for s in self.students:
                if s.name == name:
                    self.students.remove(s)
                    return True

        return False

    def check_in_student(self, student: Student = None, name: str = None, number: int = None):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_in()
                    return True

        if number != None:
            for s in self.students:
                if s.student_number == number:
                    s.check_in()
                    return True

        if name != None:
            for s in self.students:
                if s.name == name:
                    s.check_in()
                    return True

        return False

    def check_out_student(self, student: Student = None, name: str = None, number: int = None):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    s.check_out()
                    return True

        if number != None:
            for s in self.students:
                if s.student_number == number:
                    s.check_out()
                    return True

        if name != None:
            for s in self.students:
                if s.name == name:
                    s.check_out()
                    return True

        return False

    def who_is_present(self):
        temp = []

        for s in self.students:
            if s.present == True:
                temp.append(s)

        return temp

    def who_isnt_present(self):
        temp = []

        for s in self.students:
            if s.present == False:
                temp.append(s)

        return temp

    def is_student_part_of(self, student: Student = None, name: str = None, number: int = None):
        if student != None:
            for s in self.students:
                if s.name == student.name:
                    return True
        if name != None:
            for s in self.students:
                if s.name == name:
                    return True
        if number != None:
            for s in self.students:
                if s.student_number == number:
                    return True
        return False

    def format_attendance(self):
        out = []

        for s in self.students:
            out.append(s.name)

        return  out

    def format_csv(self):

        out = f"{self.name},{self.number},{self.section},{self.description},{len(self.times)},{len(self.students)},"

        str_time = "0,"
        if self.times.__len__() > 0:
            str_time = ""
            for t in self.times:
                str_time += f"{t.timestamp()};"
            str_time += ","
        out += str_time

        students = "0,"
        if self.students.__len__() > 0:
            students = ""
            for s in self.students:
                students += f"{s.student_number};"
        out += students
        return out

    def format_bytes(self):
        return str.encode(self.format_csv())

