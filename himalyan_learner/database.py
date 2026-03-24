import mysql.connector
from mysql.connector import pooling
from kivy.logger import Logger

# Connection configurations
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "SAHIL@raheja",
    "database": "himalayan_db"
}

# 1. Connection Pooling (Efficiency ke liye)
try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="himalayan_pool",
        pool_size=5,  # Ek saath 5 connections handle kar sakta hai
        **db_config
    )
    Logger.info("Database: Connection Pool created successfully")
except Exception as e:
    Logger.error(f"Database: Pool creation failed - {e}")

def get_connection():
    try:
        # Pool se connection nikalna
        connection = connection_pool.get_connection()
        if connection.is_connected():
            return connection
    except Exception as e:
        Logger.error(f"Database: Connection Error - {e}")
        
        # Fallback: Agar pool kaam na kare toh direct connection try karein
        try:
            return mysql.connector.connect(**db_config)
        except:
            return None

# 2. Check Database function (App start hote hi check karne ke liye)
def check_db_status():
    conn = get_connection()
    if conn:
        conn.close()
        return True
    return False
