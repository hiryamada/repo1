import os
import psycopg2

def check_user_exists(username, password):
    conn = None
    try:
        # DB接続情報（環境変数から取得）
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "your_db_name"),
            user=os.getenv("DB_USER", "your_db_user"),
            password=os.getenv("DB_PASSWORD", "p@ssw0rd"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
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
    
