import sqlite3


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


def get_user_history(user_id):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message, role FROM user_histories WHERE user_id = ? ORDER BY id", (user_id,))
    user_history = cursor.fetchall()
    conn.close()
    return [{"role": item[1], "content": item[0]} for item in user_history]


def add_user_message(user_id, message):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_histories (user_id, message, role) VALUES (?, ?, 'user')", (user_id, message))
    conn.commit()
    conn.close()


def add_assistant_message(user_id, message):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_histories (user_id, message, role) VALUES (?, ?, 'assistant')", (user_id, message))
    conn.commit()
    conn.close()


def clear_user_history(user_id):
    conn = sqlite3.connect('config.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_histories WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


conn = sqlite3.connect("config.db")
conn.execute("CREATE TABLE IF NOT EXISTS model_info (id INTEGER PRIMARY KEY, model_name TEXT NOT NULL)")
conn.execute("INSERT OR IGNORE INTO model_info (id, model_name) VALUES (1, 'gpt-3.5-turbo')")
conn.commit()
conn.close()

conn = sqlite3.connect("config.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS api_tokens (id INTEGER PRIMARY KEY, discord_token TEXT NOT NULL, openai_token TEXT NOT NULL)")
conn.execute("INSERT OR IGNORE INTO api_tokens (id, discord_token, openai_token) VALUES (1, '', '')")
conn.commit()
conn.close()

conn = sqlite3.connect("config.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS user_histories (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, message TEXT NOT NULL, role TEXT NOT NULL)")
conn.commit()
conn.close()
