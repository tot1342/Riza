def BD(operation: str, coin: str, amount: float, date: str):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO orders VALUES (?,?,?,?)", [(operation, coin, amount, date)])
    conn.commit()

    conn.close()
