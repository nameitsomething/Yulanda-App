from socket import socket

HOST = '3.128.156.248'
PORT = 12345

conn = socket()
conn.connect((HOST,PORT))

test_counter = 0

if __name__ == "__main__":

    # --- Login Sequence ---
    temp = int.from_bytes(conn.recv(64),"big")
    if temp == 1:
        temp = str.encode("user123,12346")
        conn.sendall(temp)
        temp = conn.recv(128)
        if temp.decode() == "posak":  # ---- End Login Sequence ----

            # --- Student Testing ---
            print("Student Add, Find, and Remove Test - Begin")

            conn.sendall(str.encode("1,0,Gabe;23;14;False"))  # Add First Student
            if conn.recv(128).decode() == "posak":
                print("Test 1 Pass")
                test_counter += 1
            else:
                print("Test 1 Fail")

            conn.sendall(str.encode("7,1,Gabe"))  # Request student info
            temp = conn.recv(128).decode()
            print(temp)

            student1 = temp.split(",")
            if student1[0] == "Gabe" and student1[1] == "23" and student1[4] == "1":  # Test Student info
                print("Test 2 Pass")
                test_counter += 1
            else:
                print("Test 2 Fail")

            conn.sendall(str.encode("2,1,Gabe"))  # Delete student
            if conn.recv(128).decode() == "posak":
                print("Test 3 Pass")
                test_counter += 1
            else:
                print("Test 3 Fail")

            # --- End Student Testing ---

            # --- Course Testing ---
            print("Course Add, Find, and Remove Test - Begin")

            conn.sendall(str.encode("3,0,M101;1;1;Lego Mechanical"))
            if conn.recv(128).decode() == "posak":
                print("Test 4 Pass")
                test_counter += 1
            else:
                print("Test 4 Fail")


            conn.sendall(str.encode("8,1,M101;1"))
            temp = conn.recv(128).decode()
            print(temp)
            if temp[0] == "M101" and temp[1] == "1" and temp[2] == "1":
                print("Test 5 Pass")
                test_counter += 1
            else:
                print("Test 5 Fail")

            conn.sendall(str.encode("4,1,M101;1"))
            if conn.recv(128).decode() == "posak":
                print("Test 6 Pass")
                test_counter += 1
            else:
                print("Test 6 fail")

            # --- End Course Testing ---

    # --- Student & Course manipulation testing ---
    if test_counter >= 5:

        print("Bulk Add & Enroll Test - Begin")

        conn.sendall(str.encode("1,0,Gabe;23;14;False"))  # Add First Student
        if conn.recv(128).decode() == "posak":  # Wait for posak
            conn.sendall(str.encode("1,0,Yulanda;16;11;False"))  # Add Second Student
            if conn.recv(128).decode() == "posak":
                conn.sendall(str.encode("1,0,Emma;10;6;False"))  # Add Third Student
                if conn.recv(128).decode() == "posak":
                    conn.sendall(str.encode("1,0,DrX;45;17;False"))  # Add Fourth Student
                    if conn.recv(128).decode() == "posak":
                        print("Test Bulk Add Passed")
                        test_counter +=1
                    else:
                        print("Fail - DrX")
                else:
                    print("Fail - Emma")
            else:
                print("Fail - Yulanda")
        else:
            print("Fail - Gabe")

        conn.sendall(str.encode("3,0,M101;1;1;Lego Mechanical"))  # Add Course
        if conn.recv(128).decode() == "posak":
            conn.sendall(str.encode("5,1,Gabe;M101;1"))  # Enroll First Student
            if conn.recv(128).decode() == "posak":
                conn.sendall(str.encode("5,1,Yulanda;M101;1"))  # Enroll Second Student
                if conn.recv(128).decode() == "posak":
                    conn.sendall(str.encode("5,1,Emma;M101;1"))  # Enroll Third Student
                    if conn.recv(128).decode() == "posak":
                        conn.sendall(str.encode("5,1,DrX;M101;1"))  # Enroll Fourth Student
                        if conn.recv(128).decode() == "posak":
                            print("Test Bulk Enroll Passed")
                            test_counter += 1
                        else:
                            print("Fail - DrX")
                    else:
                        print("Fail - Emma")
                else:
                    print("Fail - Yulanda")
            else:
                print("Fail - Gabe")
        else:
            print("Fail - Creating course")

        conn.sendall(str.encode("8,1,M101;1"))  # Get Class info
        temp = conn.recv(256).decode().split(",")
        
        if temp[0] == "M101" and temp[5] == "4":
            print("Students Successfully added to class - Test Passed")
            test_counter += 1
        else:
            print("Students not added - Test Fail")

        conn.sendall(str.encode("6,1,DrX;M101;1"))  # Remove Student from class
        if conn.recv(128).decode() == "posak":
            conn.sendall(str.encode("8,1,M101;1"))
            temp = conn.recv(256).decode().split(",")
            print(temp[7])
            if temp[5] == "3":
                print("Student Successfully removed from class - Test Passed")
                test_counter += 1
            else:
                print("Student not removed - Test Fail")

    # --- End Student & Course manipulation testing ---

    # --- Test  admin features ---

    if test_counter >= 7:
        # Write test for Schedule & attendance & Location
        conn.sendall(str.encode("9,1,Yulanda"))
        temp = conn.recv(128).decode()
        print(temp)

        conn.sendall(str.encode("10,1,M101;1"))
        temp = conn.recv(128).decode()
        print(temp)

        conn.sendall(str.encode("11,1,Yulanda"))
        temp = conn.recv(128).decode()
        print(temp)
        pass

    # --- End Test  admin features ---

    
