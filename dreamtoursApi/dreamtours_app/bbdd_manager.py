import mysql.connector

def delete_last_distance():
    mydb = get_connector()
    mydb.cursor().execute("DELETE FROM dreamtours_app_distance WHERE id = '"+str(int(get_last_distance_id()-1))+"'")
    mydb.commit()
    mydb.cursor().close()

def insert(query):
    mydb = get_connector()
    mydb.cursor().execute(query)
    mydb.commit()
    mydb.cursor().close()

def insert_distance(id, distance):
    #if not check_duplicated(distance):
    mydb = get_connector()
    mydb.cursor().execute("INSERT INTO dreamtours_app_distance VALUES ('"+id+"', '"+distance.destination+"', '"+distance.origin+"', '"+distance.distance+"')")
    mydb.commit()
    mydb.cursor().close()

def check_duplicated(distance):
    mydb = get_connector()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dreamtours_app_distance WHERE destination = '"+distance.destination+"' and origin = '"+distance.origin+"' and distance = '"+distance.distance+"'")
    myresult = mycursor.fetchall()
    mycursor.close()
    for i in myresult:
        return True
    return False

def get_last_distance_id():
    mydb = get_connector()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM dreamtours_app_distance ORDER BY id DESC")
    myresult = mycursor.fetchall()
    mycursor.close()
    for result in myresult:
        return result[0]+1
    return 1

def get_connector():
    return mysql.connector.connect(
            host="sv57.ifastnet6.org",
            user="mangasca_miguel",
            passwd="NguGujn6(3$P",
            database="mangasca_dreamtours"
    )