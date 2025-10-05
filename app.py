import psycopg2

# 生年月日から現在の年齢を計算する関数
from datetime import datetime
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
# PostgreSQL: ユーザー名とパスワードを受け取り、該当ユーザーが存在するかどうかを確認する関数
def check_user_exists(username, password):
    conn = None
    try:
        # DB接続情報（適宜書き換えてください）
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        # SQLインジェクション脆弱性を含むサンプル（教材用）
        query = f"SELECT 1 FROM users WHERE username = '{username}' AND password = '{password}' LIMIT 1;"
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        return result is not None
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        if conn:
            conn.close()
    
