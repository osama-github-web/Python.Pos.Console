# main.py
import sqlite3

# from create_table import createTable
def createTable():
    query = '''
        CREATE TABLE IF NOT EXISTS Roles
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NULL
        )
    '''

    db = sqlite3.connect('pos_db/pos.db') ## Creates a database if it does not exits
    con = db.cursor() #establishes a connection with the database
    con.execute(query) # executing a query on the database
    db.commit() # commit the query
    con.close()
    db.close() # closes the open connection

#Add User
def addRole(name):
    query = '''
        INSERT INTO Roles(name)
        VALUES(?)
    '''
    db = sqlite3.connect('pos_db/pos.db')# Creates a database if it does not exits
    conn = db.cursor() #establishes a connection with the database
    conn.execute(query, (name,))  # executing a query on the database
    db.commit() #when adding record in the database always commit it 
    conn.close()

#Update User
def updateRole(id,name):
    query = '''
        UPDATE Roles
        SET name = ?
        WHERE id = ?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (name, id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

def getAllRoles():
    query = '''
        SELECT * FROM Roles
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query)  # Execute the query with parameters
    roles = conn.fetchall()  # Commit the changes
    conn.close()  # Close the connection
    return roles

def getRole(id):
    query = '''
        SELECT * FROM Roles WHERE id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query, (id,))  # Execute the query with parameters
    role = conn.fetchone()  # Commit the changes
    conn.close()  # Close the connection
    return role

def deleteRole(id):
    query = '''
        DELETE FROM Roles WHERE id=?
    '''    
    db = sqlite3.connect('pos_db/pos.db')  # Creates a database if it does not exist
    conn = db.cursor()  # Establishes a connection with the database
    conn.execute(query,(id,))  # Execute the query with parameters
    db.commit()  # Commit the changes
    conn.close()  # Close the connection

if __name__ == "__main__":
    createTable()
    addRole('osama')
    updateRole(1,'osama')
    # deleteRole(1)

    users = getAllRoles()
    for user in users:        
        print(str(user[0:]))# Convert each user attribute to a string before concatenation

    print("Single Role")
    Role = getRole(1)
    if Role is not None:
        print(str(Role[0:])) 