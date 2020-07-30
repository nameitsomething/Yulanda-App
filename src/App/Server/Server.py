from Utils.School import School
from Utils.Student import Student
from Utils.Course import Course
from socket import socket
from threading import *
import struct

HOST = ''
PORT = 12345
server_soc = socket()
school = School()
running = True
clients = []


class Jetson(Thread):
    def __init__(self, conn: socket):
        Thread.__init__(self)
        self.conn = conn
        self.running = True

    def run(self):
        while self.running:
            self.wait_for_response()

    def wait_for_response(self):
        # In here put code for Jetson requests/Signals
        # Jetson can send information to the school in here
        packet = self.conn.recv(1024).decode().split(',')
        command = int(packet[0])
        response = str.encode("negak")

        if command == 1:
            temp = school.get_student(student_number=int(packet[1]))
            if not temp.present:
                temp.check_in()
            else:
                temp.check_out()


class User(Thread):
    def __init__(self, conn: socket):
        Thread.__init__(self)
        self.conn = conn
        self.running = True

    def run(self):
        while self.running:
            self.wait_for_request()

    def wait_for_request(self):
        # In here put code for user requests
        # User can request information from the School class through numerical commands

        packet = self.conn.recv(1024).decode().split(',')
        command = int(packet[0])
        specifier = int(packet[1])
        response = str.encode("negak")
        # Refer to command list for specification on how commands work in detail
        if command == 1:
            data = packet[2].split(';')
            temp = Student(str(data[0]), int(data[1]), int(data[2]), bool(data[3]))
            school.add_student(temp)
            response = str.encode("posak")
            self.conn.sendall(response)

        elif command == 2:
            data = packet[2].split(';')
            if specifier == 1: # Name
                if school.remove_student(name=str(data[0])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")

            elif specifier == 2: # Number
                if school.remove_student(number=int(data[0])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")

            self.conn.sendall(response)

        elif command == 3:
            data = packet[2].split(';')
            temp = Course(str(data[0]), int(data[1]), int(data[2]), str(data[3]))
            school.add_course(temp)
            response = str.encode("posak")
            self.conn.sendall(response)

        elif command == 4:
            data = packet[2].split(';')
            if specifier == 1:
                if school.remove_course(course_name=str(data[0]), course_section=int(data[1])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")
            elif specifier == 2:
                if school.remove_course(course_number=int(data[0]), course_section=int(data[1])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")
            self.conn.sendall(response)

        elif command == 5:
            data = packet[2].split(';')
            if specifier == 1:
                if school.add_student_to_course(student_name=str(data[0]), course_name=str(data[1]), course_section=int(data[2])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")
            elif specifier == 2:
                if school.add_student_to_course(student_name=str(data[0]), course_number=int(data[1]), course_section=int(data[2])):
                    response = str.encode("posak")
                else:
                    response = str.encode("negak")
            elif specifier == 3:
                if school.add_student_to_course(student_number=int(data[0]), course_name=str(data[1]), course_section=int(data[2])):
                    response = str.encoder("posak")
                else:
                    response = str.encode("negak")
            elif specifier == 4:
                if school.add_student_to_course(student_number=int(data[0]), course_number=str(data[1]), course_section=int(data[2])):
                    response = str.encode("posak")
                else:
                    response = str.encoder("negak")

            self.conn.sendall(response)

        elif command == 6:
            data = packet[2].split(';')
            if specifier == 1:
                if school.remove_student_to_course(student_name=str(data[0]), course_name=str(data[1]), course_section=int(data[2])):
                    response = "posak"
                else:
                    response = "noak"
            elif specifier == 2:
                if school.remove_student_to_course(student_name=str(data[0]), course_number=int(data[1]), course_section=int(data[2])):
                    response = "posak"
                else:
                    response = "noak"
            elif specifier == 3:
                if school.remove_student_to_course(student_number=int(data[0]), course_name=str(data[1]), course_section=int(data[2])):
                    response = "posak"
                else:
                    response = "noak"
            elif specifier == 4:
                if school.remove_student_to_course(student_number=int(data[0]), course_number=str(data[1]), course_section=int(data[2])):
                    response = "posak"
                else:
                    response = "noak"

            self.conn.sendall(response)

        elif command == 7:
            data = packet[2].split(';')
            if specifier == 1:
                temp = school.get_student(student_name=str(data[0]))
                response = temp.format_bytes()
            elif specifier == 2:
                temp = school.get_student(student_number=int(data[0]))
                response = temp.format_bytes()
            self.conn.sendall(response)

        elif command == 8:
            data = packet[2].split(';')
            if specifier == 1:
                temp = school.get_course(course_name=str(data[0]), course_section=int(data[1]))
                response = temp.format_bytes()
            elif specifier == 2:
                temp = school.get_course(course_number=int(data[0]), course_section=int(data[1]))
                response = temp.format_bytes()

        elif command == 9:
            data = packet[2].split(';')
            response = ""
            if specifier == 1:
                for c in school.courses:
                    if c.is_student_part_of(name=str(data[0])):
                        response += f"{c.name},{c.number},{c.section}"

            elif specifier == 2:
                for c in school.courses:
                    if c.is_student_part_of(number=int(data[0])):
                        response += f"{c.name},{c.number},{c.section}"

            self.conn.sendall(response)

        elif command == 10:
            data = packet[2].split(';')
            if specifier == 1:
                temp = school.get_course(course_name=str(data[0]), course_section=int(data[1]))
                response = temp.format_attendance()
            elif specifier == 2:
                temp = school.get_course(course_number=int(data[0]), course_name=int(data[1]))
                response = temp.format_attendance()
            self.conn.sendall(response)

        elif command == 11:
            data = packet.split(';')
            if specifier == 1:
                temp = school.get_student(student_name=str(data[0]))
                response = bytes(temp.present)
            elif specifier == 2:
                temp = school.get_student(student_number=int(data[0]))
                reponse = bytes(temp.present)
            self.conn.sendall(response)


def login(conn: socket):
    conn.sendall(struct.pack("B", 1))
    data = conn.recv(128).decode().split(",")

    if data[0] == "jet123" and data[1] == "12345":
        temp = Jetson(conn)
        temp.start()
        conn.sendall(str.encode("posak"))
        return temp
    elif data[0] == "user123" and data[1] == "12346":
        temp = User(conn)
        temp.start()
        conn.sendall(str.encode("posak"))
        return temp
    else:
        conn.sendall(str.encode(f"negak"))


if __name__ == '__main__':
    server_soc.bind((HOST, PORT))
    server_soc.listen(4)

    while running:
        conn, addr = server_soc.accept()
        clients.append(login(conn))
