import sqlite3


# Функции get_api_tokens и set_api_tokens добавлены для работы с токенами API
def get_api_tokens():
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("SELECT discord_token, openai_token FROM api_tokens WHERE id = 1")
    tokens = cursor.fetchone()
    conn.close()
    return tokens if tokens else (None, None)


def set_api_tokens(discord_token, openai_token):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE api_tokens SET discord_token = ?, openai_token = ? WHERE id = 1",
                   (discord_token, openai_token))
    conn.commit()
    conn.close()


def get_current_model():
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("SELECT model_name FROM model_info WHERE id = 1")
    model_name = cursor.fetchone()[0]
    conn.close()
    return model_name


def set_current_model(model_name):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE model_info SET model_name = ? WHERE id = 1", (model_name,))
    conn.commit()
    conn.close()


conn = sqlite3.connect("config.db")
conn.execute("CREATE TABLE IF NOT EXISTS model_info (id INTEGER PRIMARY KEY, model_name TEXT NOT NULL)")
conn.execute("INSERT OR IGNORE INTO model_info (id, model_name) VALUES (1, 'gpt-3.5-turbo')")
conn.commit()
conn.close()

# Создание таблицы api_tokens для хранения токенов API, если она не существует
conn = sqlite3.connect("config.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS api_tokens (id INTEGER PRIMARY KEY, discord_token TEXT NOT NULL, openai_token TEXT NOT NULL)")
conn.execute("INSERT OR IGNORE INTO api_tokens (id, discord_token, openai_token) VALUES (1, '', '')")
conn.commit()
conn.close()
