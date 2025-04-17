import psycopg2

try:
    conn = psycopg2.connect(
        dbname="sentiment_db",
        user="postgres",
        password="MySecurePass123!",
        host="sentiment-db.c7iiu0w6o6rl.eu-north-1.rds.amazonaws.com",
        port=5432
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
