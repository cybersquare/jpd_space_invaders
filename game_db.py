import MySQLdb

def login(username, user_password):
    try:
        db_connection = MySQLdb.connect(user='root', password='Your password', host='localhost', database='db_pygame')
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
        db_connection = MySQLdb.connect(user='root', password='Your password', host='localhost', database='db_pygame')
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



def save_score(score, username):
    try:
        # Create connection
        db_connection = MySQLdb.connect(user='root', password='MyNewPass', host='localhost', database='db_pygame')
        cursor = db_connection.cursor()
        sql = "SELECT user_id FROM tbl_user WHERE username = '" + username + "'"
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall() 
        userid = results[0][0]
        # Insert query
        sql = "INSERT INTO tbl_score VALUES(null, %s , %s , now())"
        val=(str(userid), str(score))
        cursor.execute(sql, val)
        # Executer query
        db_connection.commit()
        score_id=cursor.lastrowid
        # Return true after successful insertion to database
        if score_id:
            return True
    except Exception as e:
        print("Database error occurred")
        print(e)
    finally:
        db_connection.close()
    return False


def high_scores():
    try:
        # Create connection
        db_connection = MySQLdb.connect(user='root', password='MyNewPass', host='localhost', database='db_pygame')
        cursor = db_connection.cursor()

        #  query
        sql = "SELECT  full_name, score,game_day_time  FROM tbl_score join tbl_user on user_id=fk_user_id ORDER BY score DESC LIMIT 10; "
        cursor.execute(sql)
        # Executer query
        results = cursor.fetchall() 
        txt = "                    <b><u>HIGH SCORES<u></b>                   <br>"
        txt += "<b>Name           Score       Date                Time</b><br>"
        for row in results:
            txt+= str(row[0])+"         "+str(row[1])+"         "+str(row[2])[:10]+"            "+str(row[2])[10:]+"<br>"

        return txt
    except Exception as e:
        print("Database error occurred")
        print(e)
    finally:
        db_connection.close()
    return False

