# Import SQLite Module:
import sqlite3

# Create Database And Connect:
data_base = sqlite3.connect("Project.db")

# Save Data:
def save_data():
    data_base.commit()

# End Connection:
def end_connection():
    data_base.close()

# Setting Up The Cursor:
cursor = data_base.cursor()

# # Create The Lesson's Tables And Fields:
cursor.execute("""CREATE TABLE IF NOT EXISTS Lessons 
                        (LessonID INTEGER PRIMARY KEY,
                         LessonName TEXT)""")

# Create The Student's Tables And Fields:
cursor.execute("""CREATE TABLE IF NOT EXISTS Students
                        (StudentID INTEGER PRIMARY KEY,
                         FirstName TEXT,
                         LastName TEXT,
                         Age INTEGER,
                         Class TEXT,
                         DateOfRegistration TEXT)""")

# Create The School Day's Tables And Fields:
cursor.execute("""CREATE TABLE IF NOT EXISTS SchoolDay
                        (SchoolDayID INTEGER PRIMARY KEY,
                         StudentID INTEGER,
                         LessonID INTEGER,
                         FOREIGN KEY (StudentID) REFERENCES Students (StudentID),
                         FOREIGN KEY (LessonID) REFERENCES Lessons (LessonID),
                         UNIQUE (StudentID, LessonID) )""")


# Define The Show The Lessons's Tables And Fields:
def show_lessons_table():
    cursor.execute("SELECT * FROM Lessons")
    results = cursor.fetchall()
    print("\nShow Lessons's Data:")
    for row in results:
        print(f"LessonID => {row[0]}, LessonName => {row[1]}.")


# Define The Show The Students's Tables And Fields:
def show_students_table(StudentID):
    cursor.execute(f'SELECT StudentID, FirstName, LastName FROM Students WHERE StudentID = {StudentID} ')
    results = cursor.fetchall()
    print(f'\nYour StudentID [{StudentID}] Is Exists.')
    print("\nShow Students's Data:")
    for row in results:
        print(f"StudentID => {row[0]}, FirstName => {row[1]}, LastName => {row[2]}")


# Define The Show The SchoolDay's Tables And Fields:
def show_schoolday_table(StudentID, LessonID):
    cursor.execute(f"SELECT StudentID, LessonID FROM SchoolDay WHERE StudentID = {StudentID} AND LessonID = {LessonID} ")
    results = cursor.fetchall()
    print("\nShow SchoolDay's Data:")
    for row in results:
        print(f"StudentID => {row[0]}, LessonID => {row[1]}")


# Add Subjects To The Lesson's Table:
user_choose = input("If You Want To Add Lessons To The Lessons's Table, Type 'Yes' To Add, or Press 'Enter' to Cancel: ").lower().strip()
while user_choose == 'yes':  
    user_input = input('\nEnter The Lesson, Please: ').capitalize().strip()
    cursor.execute(f"""INSERT INTO Lessons
                            (LessonName)
                        VALUES
                            ('{user_input}') """)
    save_data()
    show_lessons_table()
    print('\nLessons Added \n')
    user_choose = input("If You Want To Add Another Lessons To The Lessons's Table, Type 'Yes' To Add, or Press 'Enter' to Cancel: ").lower().strip()


# Define The Add A Student Method:
def add_student():
        FirstName = input('\nEnter Your First Name, Please: ').capitalize().strip()
        LastName = input('Enter Your Last Name, Please: ').capitalize().strip()
        Age = int(input('Enter Your Age, Please: '))
        Class = input('Enter Your Class, Please: ').capitalize().strip()
        DateOfRegistration = input('Enter Your Date Of Registration Like "4/10/2024", Please: ').strip()
        cursor.execute(f"""INSERT INTO Students
                                (FirstName, LastName, Age, Class, DateOfRegistration)
                            VALUES 
                                ('{FirstName}', '{LastName}', {Age}, '{Class}', '{DateOfRegistration}')""")
        save_data()
        print('The Operation Was Successful 👍. \n')


# Define The Add A StudentID And LessonID Method:
def add_StudentID_and_LessonID():
    
    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_StudentID_Check = cursor.fetchall()
    if Result_Of_StudentID_Check[0][0] == 1:

        # Display The SchoolDay's Table For StudentID:
        cursor.execute(f"""SELECT
                            Students.StudentID,
                            Students.FirstName,
                            Students.LastName,
                            Lessons.LessonID,
                            Lessons.LessonName
                        FROM 
                            Students
                        INNER JOIN
                            SchoolDay ON  Students.StudentID = SchoolDay.StudentID
                        INNER JOIN  
                            Lessons ON SchoolDay.LessonID = Lessons.LessonID
                        WHERE 
                            Students.StudentID = {StudentID} """)
        Result = cursor.fetchall()
        for row in Result:
            print(f"\nStudent's Information Data: \nStudentID => {row[0]}.\nFirstName => {row[1]}. \nLastName => {row[2]}. \n\nLesson's Information Data: \nLessonID => {row[3]}. \nLessonName => {row[4]}. \n\n----------------------------------")
        # Display The Lessons's Table For A Student:
        show_lessons_table()

        # Check IF LessonID Is Exists In The Lessons's Table:
        cursor.execute(f"SELECT COUNT(*) FROM Lessons")
        Result_Of_LessonID_Check = cursor.fetchall()
        Result_Of_LessonID_Check = Result_Of_LessonID_Check[0][0]
        LessonID = int(input('\nNow You Can Choose The Lesson By Pressing The Number: '))
        if LessonID > 0 and LessonID <= Result_Of_LessonID_Check:

            # Check IF LessonID Is Exists In The SchoolDay's Table:
            cursor.execute(f"SELECT COUNT(*) FROM SchoolDay WHERE StudentID = {StudentID} AND LessonID = {LessonID}")
            Result = cursor.fetchall()
            if Result[0][0] != 1:
                cursor.execute(f"""INSERT INTO SchoolDay
                                        (StudentID, LessonID)
                                    VALUES
                                            ({StudentID}, {LessonID})""")
                save_data()
                print('The Operation Was Successful 👍 \n')
            else:
                print(f"Your LessonID [{LessonID}] Is Already Exists.")
        else:
            print(f"LessonID [{LessonID}] Is Not Aviable.\n")
    else:
        print(f"Your StudentID [{StudentID}] Is Not Available\n ")



# Define The Delete A Student Method:
def delete_student():

    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_Check = cursor.fetchall()
    if Result_Of_Check[0][0] == 1:
            show_students_table(StudentID)
            cursor.execute(f"""DELETE FROM SchoolDay
                        WHERE
                            StudentID = {StudentID}""")

            cursor.execute(f"""DELETE FROM Students
                        WHERE
                            StudentID = {StudentID}""")
            save_data()
            print('\nThe Operation Was Successful 👍 \n')
    else:
        print(f"Your StudentID [{StudentID}] Is Not Available\n ")



# Define The Delete A Lesson Method:
def delete_lesson():
    
    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_Check = cursor.fetchall()
    if Result_Of_Check[0][0] == 1:

        # Display The SchoolDay's Table For StudentID:
        cursor.execute(f"""SELECT
                            Students.StudentID,
                            Students.FirstName,
                            Students.LastName,
                            Lessons.LessonID,
                            Lessons.LessonName
                        FROM 
                            Students
                        INNER JOIN
                            SchoolDay ON  Students.StudentID = SchoolDay.StudentID
                        INNER JOIN  
                            Lessons ON SchoolDay.LessonID = Lessons.LessonID
                        WHERE 
                            Students.StudentID = {StudentID} """)
        Result = cursor.fetchall()
        for row in Result:
            print(f"\nStudent's Information Data: \nStudentID => {row[0]}.\nFirstName => {row[1]}. \nLastName => {row[2]}. \n\nLesson's Information Data: \nLessonID => {row[3]}. \nLessonName => {row[4]}. \n\n----------------------------------")

        
        # Display The Lessons's Table For The Student:
        show_lessons_table()
        
        # Check IF LessonID Is Exists In The Lessons's Table:
        cursor.execute(f"SELECT COUNT(*) FROM Lessons")
        Result_Of_LessonID_Check = cursor.fetchall()
        Result_Of_LessonID_Check = Result_Of_LessonID_Check[0][0]
        LessonID = int(input('\nNow You Can Choose The Lesson By Pressing The Number: '))
        if LessonID > 0 and LessonID <= Result_Of_LessonID_Check:

            # Check IF LessonID Is Exists In The SchoolDay's Table:
            cursor.execute(f"SELECT COUNT(*) FROM SchoolDay WHERE StudentID = {StudentID} AND LessonID = {LessonID}")
            Result = cursor.fetchall()
            if Result[0][0] == 1:
                show_schoolday_table(StudentID, LessonID)
                cursor.execute(f"""DELETE FROM SchoolDay WHERE StudentID = {StudentID} AND LessonID = {LessonID}""")
                save_data()
                print('\nThe Operation Was Successful 👍 \n')

            else:
                print(f"LessonID [{LessonID}] Is Not Aviable\n")

        else:
            print(f"LessonID [{LessonID}] Is Not Aviable\n")
        
    else:
        print(f"\nYour StudentID [{StudentID}] Is Not Available.")
         

# Define The Update A Student Method:
def update_student():
    
    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_Check = cursor.fetchall()
    if Result_Of_Check[0][0] == 1:

        # Display The Students's Table For The Student:
        show_students_table(StudentID)

        FirstName = input('\nEnter Your First Name, Please: ').capitalize().strip()
        LastName = input('Enter Your Last Name, Please: ').capitalize().strip()
        Age = int(input('Enter Your Age, Please: '))
        Class = input('Enter Your Class, Please: ').capitalize().strip()
        DateOfRegistration = input('Enter Your Date Of Registration Like "4/10/2024", Please: ').strip()
        cursor.execute(f"""UPDATE Students
                            SET
                                FirstName = '{FirstName}',
                                LastName = '{LastName}',
                                Age = {Age},
                                Class = '{Class}',
                                DateOfRegistration = '{DateOfRegistration}'
                            WHERE
                                StudentID = {StudentID}""")
        save_data()
        print('The Operation Was Successful 👍 \n')
    
    else:
        print(f"Your StudentID [{StudentID}] Is Not Available\n ")




# Define The Update A Lesoon Method:
def update_lesson():

    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_Check = cursor.fetchall()
    if Result_Of_Check[0][0] == 1:

            # Display The SchoolDay's Table For The Student:
            cursor.execute(f"""SELECT
                                Students.StudentID,
                                Students.FirstName,
                                Students.LastName,
                                Lessons.LessonID,
                                Lessons.LessonName
                            FROM 
                                Students
                            INNER JOIN
                                SchoolDay ON  Students.StudentID = SchoolDay.StudentID
                            INNER JOIN  
                                Lessons ON SchoolDay.LessonID = Lessons.LessonID
                            WHERE 
                                Students.StudentID = {StudentID} """)
            Result = cursor.fetchall()
            for row in Result:
                print(f"\nStudent's Information Data: \nStudentID => {row[0]}.\nFirstName => {row[1]}. \nLastName => {row[2]}. \n\nLesson's Information Data: \nLessonID => {row[3]}. \nLessonName => {row[4]}. \n\n----------------------------------")
            
            # Display The Lessons's Table For The Student:
            show_lessons_table()

            # Check IF Old_LessonID Is Exists In The SchoolDay's Table:
            Old_LessonID = int(input('\nNow You Can Replace The Old Lesson By Pressing The Number: '))
            cursor.execute(f"SELECT COUNT(*) FROM SchoolDay WHERE StudentID = {StudentID} AND LessonID = {Old_LessonID}")
            Result_Of_Check_the_Old_LessonID = cursor.fetchall()
            if Result_Of_Check_the_Old_LessonID[0][0] == 1: 
                
                # Check IF New_LessonID Is Exists In The Lessons's Table:
                New_LessonID = int(input('\nNow You Can Set The New Lesson By Pressing The Number: '))
                cursor.execute(f"SELECT COUNT(*) FROM Lessons WHERE LessonID = {New_LessonID}")
                Result_Of_Check_the_new_LessonID = cursor.fetchall()
                if Result_Of_Check_the_new_LessonID[0][0] == 1:
                    cursor.execute(f"""UPDATE SchoolDay
                                    SET LessonID = {New_LessonID}
                                    WHERE StudentID = {StudentID} AND LessonID = {Old_LessonID} """)
                    save_data()
                    print('The Operation Was Successful 👍 \n')
                else:
                    print(f"Your LessonID [{New_LessonID}] Is Not Available")
            else:
                print(f"Your LessonID [{Old_LessonID}] Is Not Available")
    else:
        print(f"Your StudentID [{StudentID}] Is Not Available\n")


# Define The Show A Student Information Method:
def show_student_information():
    
    # Check IF StudentID Is Exists In The Students's Table:
    StudentID = int(input('\nEnter Your StudentID Number, Please: '))
    cursor.execute(f"SELECT COUNT(*) FROM Students WHERE StudentID = {StudentID}")
    Result_Of_Check = cursor.fetchall()
    if Result_Of_Check[0][0] == 1:
        
        # Display The Students's Table For The Student:
        show_students_table(StudentID)

        # Display The SchoolDay's Table For The Student:
        cursor.execute(f"""SELECT
                            Students.StudentID,
                            Students.FirstName,
                            Students.LastName,
                            Lessons.LessonID,
                            Lessons.LessonName
                        FROM 
                            Students
                        INNER JOIN
                            SchoolDay ON  Students.StudentID = SchoolDay.StudentID
                        INNER JOIN  
                            Lessons ON SchoolDay.LessonID = Lessons.LessonID
                        WHERE 
                            Students.StudentID = {StudentID} """)
        Result = cursor.fetchall()
        for row in Result:
            print(f"\nStudent's Information Data: \nStudentID => {row[0]}.\nFirstName => {row[1]}. \nLastName => {row[2]}. \n\nLesson's Information Data: \nLessonID => {row[3]}. \nLessonName => {row[4]}. \n\n----------------------------------")
    else:
        print(f"Your StudentID [{StudentID}] Is Not Available\n ")
    

# Command's Options List:
commands_list = ["a", "d", "u", "s", "q"]

# Input Big Message For The User:
input_message = '''
    ***** Welcome To The School System ***** 
        To Add A Student, Press "a".
        To Delete A Student, Press "d".
        To Update A Student, press "u".
        To Show A Student's Information, Press "s".
        To Quit The Program, Press "q".

Choose Option: '''

# Input Option Choose From The User:
user_input = input(input_message).lower().strip()

# Check If Command Is Exists
while user_input in commands_list:

    # When The User Press 'a':
    while user_input == 'a':
        
        user_choose = input("\nDo You Want To Add A New Student? Type 'Yes' To Add, Or Press'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            add_student()
            user_choose = input("Do You Want To Add Another Student? Type 'Yes' To Add, Or Press 'Enter' To Cancel: ").lower().strip()
        
        user_choose = input("\nDo You Want To Add Subjects? Type 'Yes' To Add, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            add_StudentID_and_LessonID()
            user_choose = input("Do You Want To Add Another Subjects? Type 'Yes' To Add, Or Press 'Enter' To Cancel: ").lower().strip()
        user_input = input(input_message).lower().strip()

    # When The User Press 'd'
    while user_input == 'd':
        
        user_choose = input("\nDo You Want To Delete A Student? Type 'Yes' To Delete, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            delete_student()
            user_choose = input("Do You Want To Delete Another Student? Type 'Yes' To Delete, Or Press 'Enter' To Cancel: ").lower().strip()
        
        user_choose = input("\nDo You Want To Delete A Subjects? Type 'Yes' To Delete, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            delete_lesson()
            user_choose = input("\nDo You Want To Delete Another Subjects? Type 'Yes' To Delete, Or Press 'Enter' To Cancel: ").lower().strip()
        user_input = input(input_message).lower().strip()

    # When The User Press 'u'
    while user_input == 'u':
        user_choose = input("\nDo You Want To Update A Student? Type 'Yes' To Update, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            update_student()
            user_choose = input("Do You Want To Update Anohter Student? Type 'Yes' To Update, Or Press 'Enter' To Cancel: ").lower().strip()
        
        user_choose = input("\nDo You Want To Update A Subject? Type 'Yes' To Update, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            update_lesson()
            user_choose = input("\nDo You Want To Update Another Subject? Type 'Yes' To Update, Or Press 'Enter' To Cancel: ").lower().strip()
        user_input = input(input_message).lower().strip()

    # When The User Press 's'
    while user_input == 's':
        user_choose = input("\nDo You Want To Show A Student's Information? Type 'Yes' To Show, Or Press 'Enter' To Cancel: ").lower().strip()
        while user_choose == 'yes':
            show_student_information()
            user_choose = input("\nDo You Want To Show Another Student's Information? Type 'Yes' To Show, Or Press 'Enter' To Cancel: ").lower().strip()
        
        user_input = input(input_message).lower().strip()

    # When The User Press 'q'
    if (user_input == 'q'):
        end_connection()
        print('\nProgram Is Closed.\n')
        print('\nGood Bye.\n')
        end_connection()
        break


while user_input not in commands_list:
    print(f'\nSorry, This Command [{user_input}] Is Not Found"')
    user_input = input(input_message).lower().strip()
