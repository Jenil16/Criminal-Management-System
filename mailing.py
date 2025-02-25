import smtplib
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='root', database='management')
my_cursor = conn.cursor()
my_cursor2 = conn.cursor()
my_cursor.execute("select Email from police where Area='Panigate';");
my_cursor2.execute("")
receiver_email = ""
for i in my_cursor:
    print(i);
    receiver_email = i;
print(receiver_email);
conn.commit()
my_cursor.close();
conn.close();


sender_email = "pjenil1609@gmail.com"
password = "kdztqgnrykyapbmy"
message = """\
Subject: Criminal Detected

Details : """

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
