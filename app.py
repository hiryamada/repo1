def check_user_exists(username, password):
    conn = None
    try:
        # DB接続情報（適宜書き換えてください）
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="p@ssw0rd",
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
    
