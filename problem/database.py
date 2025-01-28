import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your-password",
    database = "hopedatacenter"
)

cursor = db.cursor()
table_name = 'users'

def get_num_of_users():
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)

    users_count = cursor.fetchone()[0]
    return users_count

def add_user_to_database(user):
    try:
        query = f"INSERT INTO {table_name} (id, username, password, email) VALUES ({user.id}, '{user.name}', '{user.password}', '{user.email}')"
        cursor.execute(query)
        db.commit()  # Commit the transaction
        print('User added to database')
    except Exception as e:
        print(f"Error adding user to database: {e}")
        db.rollback()  # Rollback the transaction in case of an error

def get_acctual_password(username):
    try:
        query = "SELECT password FROM users WHERE username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()[0] 

        if result:
            print('User found')
            return result
        else:
            print('User not found')
            return -1
    except Exception as e:
        print(f"Error querying the database: {e}")
        return -1 
    
def is_username_in_database(username):
    try:
        query = "SELECT password FROM users WHERE username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()[0] 

        if result:
            print('User found')
            return True
        else:
            print('User not found')
            return False 
    except Exception as e:
        return False