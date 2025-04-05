import psycopg2
    # создаем БД
# conn = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="!P@ssw0rd", port="5432")
# cursor = conn.cursor()
# conn.autocommit = True  # команда для создания базы данных
# cursor.execute("CREATE DATABASE test2")
# print("База данных успешно создана")
# cursor.close()
# conn.close()


conn = psycopg2.connect(dbname="test2", host="localhost", user="postgres", password="!P@ssw0rd", port="5432")
cursor = conn.cursor()
    # создаем таблицу
# cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# conn.commit()  # поддверждаем транзакцию
# print("Таблица people успешно создана")

#     # вносим данные в таблицу
# bob = ("Bob", 42)
# cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)
# # cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")  # 2сп
# people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
# cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)  # Множественная вставка
# conn.commit()  # выполняем транзакцию
# print("Данные добавлены")



    # получаем все данные из таблицы people
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())  # список кортежей
# print(cursor.fetchmany(3))  # часть списка кортежей
# print(cursor.fetchone())    # один кортеж из списка

for person in cursor:
# for person in cursor.fetchall():  # 2 сп
    print(f"{person[1]} - {person[2]}")
#
cursor.execute("SELECT name, age FROM people WHERE id=4")
name, age = cursor.fetchone()  # раскладываем кортеж на две переменных
print(f"Name: {name}    Age: {age}")    # Name: Bob   Age: 42

#     # обновляем данные
# cursor.execute("UPDATE people SET name ='Tomas' WHERE name='Bob'")
# # cursor.execute("UPDATE people SET name =%s WHERE name=%s", ("Tomas", "Tom"))
# conn.commit()
#     # delete
# cursor.execute("DELETE FROM people WHERE name=%s", ("Tomas",))
# conn.commit()
#     # delete many
# people = [(3,), (5,)]
# cursor.executemany("DELETE FROM people WHERE id=%s", people)
# conn.commit()


cursor.close()
conn.close()

