import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="db_mining_1"
)

cursor = conn.cursor()

# --- QUERY 1: Select all products ---
print("--- 📦 DISPLAYING PRODUCTS ---")
cursor.execute("SELECT * FROM products")
all_products = cursor.fetchall()

for row in all_products:
    # row[0] is ID, row[1] is Name, row[2] is Price
    print(f"Product ID: {row[0]} | Name: {row[1]} | Price: ${row[2]}")

print("\n")

# --- QUERY 2: Select specific user (evan_j) ---
print("--- 👤 FINDING USER 'evan_j' ---")
cursor.execute("SELECT id, username, email FROM users WHERE username='evan_j';")
user_data = cursor.fetchall()

if len(user_data) > 0:
    for row in user_data:
        user_id = row[0]
        username = row[1]
        email = row[2]
        print(f"User #{user_id} has the username: '{username}' (Contact: {email})")
else:
    print("User not found.")

# Close the connection
cursor.close()
conn.close()