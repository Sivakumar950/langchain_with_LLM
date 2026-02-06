import sqlite3

conn= sqlite3.connect('salesDB/sales.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                sale_date DATE NOT NULL
               )
        ''')
cursor.execute('''INSERT INTO sales (customer_name, product_name, quantity, price, sale_date)
                VALUES ('John Doe', 'Laptop', 1, 999.99, '2024-01-15'),
                       ('Jane Smith', 'Smartphone', 2, 499.99, '2024-01-16'),
                       ('Alice Johnson', 'Headphones', 3, 199.99, '2024-01-17'),
                          ('Bob Brown', 'Monitor', 1, 299.99, '2024-01-18'),
                          ('Charlie Davis', 'Keyboard', 5, 49.99, '2024-01-19'),
                            ('Eve Wilson', 'Mouse', 4, 29.99, '2024-01-20'),
                            ('Frank Miller', 'Printer', 1, 149.99, '2024-01-21'),
                            ('Grace Lee', 'Webcam', 2, 89.99, '2024-01-22'),
                            ('Hank Green', 'External Hard Drive', 1, 129.99, '2024-01-23')
                ''')
cursor.execute('''SELECT * FROM sales''')
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.commit()