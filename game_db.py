import MySQLdb

def login(username, user_password):
    try:
        db_connection = MySQLdb.connect(user='root', password='MyNewPass', host='localhost', database='db_pygame')
        cursor = db_connection.cursor()
        sql = "select * from tbl_user where username = %s and password = %s"
        val=(username, user_password)
        cursor.execute(sql, val)
        results = cursor.fetchall() 
        if results:
            return True
            
    except Exception as e:
        print("Database error occured")
        print(e)
    return False


def register(username, user_password, name, gender):
    try:
        db_connection = MySQLdb.connect(user='root', password='MyNewPass', host='localhost', database='db_pygame')
        cursor = db_connection.cursor()
        sql = "INSERT INTO tbl_user(username, password, full_name, gender) VALUES(%s, %s, %s, %s )"
        val=(username, user_password, name, gender)
        cursor.execute(sql, val)
        db_connection.commit()
        user_id=cursor.lastrowid
        db_connection.close()
        if user_id:
            return True
    except Exception as e:
        print("Database error occured")
        print(e)
    return False