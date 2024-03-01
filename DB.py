import sqlite3

# Подключение к базе данных (если базы не существует, она будет создана)
conn = sqlite3.connect('example.db')

# Создание курсора для выполнения операций с базой данных
cur = conn.cursor()

# Пример создания таблицы
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT
            )''')

# Пример вставки данных в таблицу
def insert_user(username, first_name, last_name):
    cur.execute("INSERT INTO users (username, first_name, last_name) VALUES (?, ?, ?)", (username, first_name, last_name))
    conn.commit()

# Пример выборки данных из таблицы
def get_users():
    cur.execute("SELECT * FROM users")
    return cur.fetchall()

# Закрытие курсора и соединения с базой данных
def close_db():
    cur.close()
    conn.close()

# Пример использования функций для работы с базой данных
if __name__ == '__main__':
    # Добавление пользователей
    insert_user('user1', 'John', 'Doe')
    insert_user('user2', 'Jane', 'Smith')

    # Получение пользователей и вывод на экран
    users = get_users()
    for user in users:
        print(user)

    # Закрытие базы данных
    close_db()
