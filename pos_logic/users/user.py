# main.py
import sqlite3

# from create_table import createTable
def createTable():
    query = '''
        CREATE TABLE IF NOT EXISTS Users
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_id INTEGER NULL, 
            name TEXT NULL,
            email TEXT NULL,
            phone TEXT NULL
        )
    '''

    db = sqlite3.connect('pos_db/pos.db') ## Creates a database if it does not exits
    con = db.cursor() #establishes a connection with the database
    con.execute(query) # executing a query on the database
    db.commit() # commit the query
    con.close()
    db.close() # closes the open connection

#Add User
def addUser(name,email,phone):
    query = '''
        INSERT INTO Users(name,email,phone)
        VALUES(? ,? , ?)
    '''
    db = sqlite3.connect('pos_db/pos.db')# Creates a database if it does not exits
    conn = db.cursor() #establishes a connection with the database
    conn.execute(query, (name,email,phone))  # executing a query on the database
    db.commit() #when adding record in the database always commit it 
    conn.close()

#Update User
def updateUser(name, email, phone):
    query = '''
        UPDATE Users
        SET email = ?, phone = ?
        WHERE name = ?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (email, phone, name))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

def getAllUsers():
    query = '''
        SELECT * FROM Users
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query)  # Execute the query with parameters
    users = conn.fetchall()  # Commit the changes
    conn.close()  # Close the connection
    return users

def getUser(id):
    query = '''
        SELECT * FROM Users WHERE id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (id,))  # Execute the query with parameters
    users = conn.fetchone()  # Commit the changes
    conn.close()  # Close the connection
    return users

def deleteUser(id):
    query = '''
        DELETE FROM Users WHERE id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query,(id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

def addRoleToUser(user_id, role_id):
    query = '''
        UPDATE Users
        SET role_id = ? 
        WHERE id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query,(role_id, user_id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection


if __name__ == "__main__":
    createTable()
    addUser('osama','osama','osama')
    updateUser('osama','ASDASDF','ASDFASDFASDF')
    addRoleToUser(2,1)

    users = getAllUsers()
    for user in users:        
        print(str(user[0:]))# Convert each user attribute to a string before concatenation

    print("Single User")
    user = getUser(3)
    if user is not None:
        print(str(user))