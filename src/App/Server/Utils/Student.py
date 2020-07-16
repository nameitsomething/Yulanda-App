class Student:

    def __init__(self, name: str, age: int, grade: int, present: bool):
        self.name = name
        self.age = age
        self.grade = grade
        self.present = present
        self.student_number = 0

    def set_student_number(self, number: int):
        if self.student_number == 0:
            self.student_number = number

    def check_in(self):
        if not self.present:
            self.present = True

    def check_out(self):
        if self.present:
            self.present = False

    def format_csv(self):
        return f"{self.name},{self.age},{self.grade},{self.present},{self.student_number}"

    def format_bytes(self):
        return str.encode(self.format_csv())

    def get_info(self):
        return [self.name, self.age, self.present, self.student_number]
