import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1", user="root", password="root", database="db_mining_1"
)
cursor = conn.cursor()

# insert new user
sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
val = ("juan_dela_cruz", "juan@email.com")
cursor.execute(sql, val)

# save changes on database
conn.commit() 

print(f"✅ {cursor.rowcount} record inserted. Juan is now added!")

cursor.close()
conn.close()