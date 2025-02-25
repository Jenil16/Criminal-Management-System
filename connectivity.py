import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='management')
my_cursor = conn.cursor()
my_cursor.execute("select Email from police where Area='Panigate';");
for i in my_cursor:
    print(i);
conn.commit()
my_cursor.close();
conn.close();