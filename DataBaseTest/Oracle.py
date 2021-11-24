import cx_Oracle
connection = cx_Oracle.connect('book_ex/book_ex@XE')
cursor = connection.cursor()
querystring = "SELECT * FROM BOARD"
cursor.execute(querystring)
print(cursor.fetchall())
cursor.close()
connection.close()