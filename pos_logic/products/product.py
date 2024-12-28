# main.py
import sqlite3

# from create_table import createTable
def createTable():
    query = '''
        CREATE TABLE IF NOT EXISTS Products
        (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NULL, 
            price FLOAT NOT NULL, 
            stock_quantity INT NULL
        )
    '''

    db = sqlite3.connect('pos_db/pos.db') ## Creates a database if it does not exits
    con = db.cursor() #establishes a connection with the database
    con.execute(query) # executing a query on the database
    db.commit() # commit the query
    con.close()
    db.close() # closes the open connection

#Add User
def addProduct(name, category, price, stock_quantity):
    query = '''
        INSERT INTO Products(name, category, price, stock_quantity)
        VALUES(?, ?, ?, ?)
    '''
    db = sqlite3.connect('pos_db/pos.db')# Creates a database if it does not exits
    conn = db.cursor() #establishes a connection with the database
    conn.execute(query, (name, category, price, stock_quantity))  # executing a query on the database
    db.commit() #when adding record in the database always commit it 
    conn.close()

#Update User
def updateProduct(product_id, name, category, price, stock_quantity):
    query = '''
        UPDATE Products
        SET name = ?, category = ?, price = ?, stock_quantity = ?
        WHERE product_id = ?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (name, category, price, stock_quantity, product_id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

def getAllProduct():
    query = '''
        SELECT * FROM Products
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query)  # Execute the query with parameters
    products = conn.fetchall()  # Commit the changes
    conn.close()  # Close the connection
    return products

def getProduct(product_id):
    query = '''
        SELECT * FROM Products WHERE product_id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (product_id,))  # Execute the query with parameters
    products = conn.fetchone()  # Commit the changes
    conn.close()  # Close the connection
    return products

def deleteProduct(product_id):
    query = '''
        DELETE FROM Roles WHERE product_id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query,(product_id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

if __name__ == "__main__":
    createTable()
    addProduct('Cake', 'Store_Item', 50, 25)
    updateProduct(1, 'Updated Laptop', 'Electronics', 899.99, 5)  # Update an existing product
    # deleteRole(1)

    Products = getAllProduct()
    for product in Products:        
        print(str(product[0:]))# Convert each user attribute to a string before concatenation

    print("Single Role")
    Product = getProduct(1)
    if Product is not None:
        print(str(Product[0:])) 