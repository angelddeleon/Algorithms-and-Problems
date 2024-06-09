import mysql.connector

conexion = mysql.connector.connect(user='root', password='#Lo28de06',
                                    host='localhost',
                                    database='hello_mysql')

print(conexion)

cursor = conexion.cursor()

sql = ("INSERT INTO students(id_student, name_student, phone_student, subject_student, grades_student ) VALUES(%s, %s, %s, %s, %s)")
val = ( 2 ,"David", 5 , "Alge", "0")

cursor.execute(sql, val)

conexion.commit()



cursor.execute("SELECT * FROM students")

myresult = cursor.fetchall()

for x in myresult:
  print(x)


#Create A Student and save it in a DB

#Creating class Student

class Student:

    def __init__(self, id , name, phoneNumber, subject, grades):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.grades = []

    def __str__(self):
        return f"{self.name} {self.phoneNumber} {self.subject} {self.grades}"

    def addGrades(self, grades):
        self.grades += [grades]


p1 = Student( 1 ,"Angel", 4144394532 , "Calculo", 0)

p1.addGrades(10)
p1.addGrades(20)

print(p1)




