import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4132",
        database="student_task_manage"
        )
    return connection