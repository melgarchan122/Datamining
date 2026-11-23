import mysql.connector

try:
    
    print("Connecting to database...")
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",  # password 
        database="db_mining_1"
    )
    
    if conn.is_connected():
        print("✅ Connected successfully!\n")
        
        # 2. Read users table
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        print(f"--- 👥 USERS (Total: {len(users)}) ---")
        for row in users:
            print(f"ID: {row[0]} | Username: {row[1]} | Email: {row[2]}")
            
        print("\n")
        
        # 3. Reads products table
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        
        print(f"--- 📦 PRODUCTS (Total: {len(products)}) ---")
        for row in products:
            print(f"ID: {row[0]} | Name: {row[1]} | Price: ${row[2]}")
            
        # 4. Close connection
        cursor.close()
        conn.close()
        print("\n🔒 Connection closed.")

except mysql.connector.Error as e:
    print(f"❌ Error: {e}")