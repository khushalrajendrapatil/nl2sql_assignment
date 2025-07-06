import sqlite3

def create_database():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS customers")
    cursor.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT
        )
    """)

    customers = [
        (1, "Amit", "Delhi"),
        (2, "Ravi", "Mumbai"),
        (3, "Neha", "Delhi")
    ]
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    create_database()
