import psycopg2
import csv


conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="aibek2006"
)

cur = conn.cursor()
if conn.closed:
    print("Соединение с базой данных закрыто.")
else:
    print("Приложение подключено к базе данных.")



def inputData():
    name = input("Введите ваше имя: ")
    number = input("Введите ваш номер телефона: ")
    cur.execute('INSERT INTO phonebook("personname", "phonenumber") VALUES (%s, %s);', (name, number))
    conn.commit()

def importFromCSV():
    with open("aaaa.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO phonebook("PersonName", "PhoneNumber") VALUES (%s, %s);', (personName, phoneNumber))
    conn.commit()

def update_contact(PersonName, PhoneNumber):
    cur.execute('UPDATE phonebook SET phonenumber = %s WHERE personname = %s;', (PhoneNumber, PersonName))
    conn.commit()


def queryData():
    cur.execute('SELECT * FROM phonebook;')
    data = cur.fetchall()
    with open("queredData.txt", "w") as f:
        for row in data:
            f.write(f"Name: {row[1]}\nNumber: {row[2]}\n")


def deleteData():
    personName = input("Какое имя вы хотите удалить?\n")
    cur.execute(f'DELETE FROM phonebook WHERE "personname" = %s;', (personName,))
    conn.commit()


def deleteAllData():
    cur.execute('DELETE FROM phonebook;')
    conn.commit()


while True:
    print("Что вы хотите сделать?\n\
          1. Ввести данные вручную\n\
          2. Загрузить из файла CSV\n\
          3. Обновить существующий контакт\n\
          4. Запросить данные из таблицы\n\
          5. Удалить данные по имени\n\
          6. Удалить все данные из таблицы\n\
          ")

    choice = input("Введите номер действия (1-5):\n")
    if choice == '1':
        inputData()
    elif choice == '2':
        importFromCSV()
    elif choice == '3':
        name = input("Введите имя и новый номер через пробел: ").split()
        update_contact(*name)
    elif choice == '4':
        queryData()
    elif choice == '5':
        deleteData()
    elif choice == '6':
        deleteAllData()

cur.close()
conn.close()
