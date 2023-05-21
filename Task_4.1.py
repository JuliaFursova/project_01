# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# connection = sqlite3.connect('C:/Users/User/Desktop/Учеба Юля/teachers.db')
# сursor = connection.cursor()
# sqlquery = """CREATE TABLE Students 
# (Student_Id INTEGER,
# Student_Name TEXT,
# School_Id INTEGER PRIMARY KEY);"""

# сursor.execute(sqlquery)
# connection.commit()
# connection.close()

# connection = sqlite3.connect('C:/Users/User/Desktop/Учеба Юля/teachers.db')
# сursor = connection.cursor()
# sqlquery = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Петр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);"""

# сursor.execute(sqlquery)
# connection.commit()
# connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('C:/Users/User/Desktop/Учеба Юля/teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_student_detail(Student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    sqlquery = "SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?"
    cursor.execute(sqlquery,(Student_id,))
    record = cursor.fetchall()
    for row in record:
      print ("ID студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", row[3], "\n")
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Ошибка в получении данных ", error)

get_school_student_detail(204)

