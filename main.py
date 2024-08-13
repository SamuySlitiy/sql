import sqlite3

connect = sqlite3.connect("college.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               major TEXT NOT NULL
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT NOT NULL,
               instructor TEXT NOT NULL
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY(student_id) REFERENCES students(id),
               FOREIGN KEY(course_id) REFERENCES courses(id)
               )
''')

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Input name:")
        age = int(input("Input age:"))
        major = input("Input spec:")
        cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
        connect.commit()
        # Додавання нового студента

    elif choice == "2":
        pass
    # Додавання нового курсу

    elif choice == "3":
        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()
        print(students)
        # Показати список студентів
     
    elif choice == "4":
        pass
        # Показати список курсів

    elif choice == "5":
        pass
        # Зареєструвати студента на курс

    elif choice == "6":
        pass
        # Показати студентів на конкретному курсі
       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")