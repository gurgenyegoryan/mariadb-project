import mariadb
import sys

# Connect to MariaDB Platform

try:
    conn = mariadb.connect(
        user="root",
        password="Yeg.1995",
        host="ngn.am",
        port=3306,
        database="pythontest",
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

