from tkinter import StringVar
from xmlrpc.client import DateTime
import face_recognition
import cv2
import mysql
import numpy as np
import csv
import geocoder
import os
from datetime import datetime
import smtplib
import mysql.connector
import self as self
from geopy.geocoders import Nominatim
import mysql.connector as connect


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


import smtplib
import mimetypes
from email.message import EmailMessage

video_capture = cv2.VideoCapture(0)

jenil_image = face_recognition.load_image_file("photos/Jenil.jpg")
jenil_encoding = face_recognition.face_encodings(jenil_image)[0]

neer_image = face_recognition.load_image_file("photos/Neer.jpg")
neer_encoding = face_recognition.face_encodings(neer_image)[0]

shivam_image = face_recognition.load_image_file("photos/Shivam.jpg")
shivam_encoding = face_recognition.face_encodings(shivam_image)[0]


known_face_encoding = [

    jenil_encoding,
    neer_encoding,
    shivam_encoding

]

known_faces_names = [

    "Jenil",
    "Neer",
    "Shivam"

]

students = known_faces_names.copy()

face_location = []
face_encoding = []
face_names = []
s = True


now = datetime.now()
current_date = now.strftime("%Y-%m-%d")


f = open(current_date+'.csv', 'w+', newline='')
lnwriter = csv.writer(f)

geolocator = Nominatim(user_agent="geoapiExercises")

while True:
    a = ""
    b = ""
    c = ""
    f = ""
    g = ""
    h = ""
    q = ""
    i = "CAM1"
    j = ""
    k = ""
    z = "CAM1"
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(
                known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(i)
                    j = name
                    print(name)

                    g = geocoder.ip('me')
                    location = g.latlng
                    k = location
                    print(location)
                    # loc = geolocator.reverse(location[0]+ "," +location[1])
                    # print(loc)
                    current_time = now.strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time, location])

                    conn = mysql.connector.connect(
                        host='localhost', user='root', password='root', database='management')
                    my_cursor2 = conn.cursor(prepared=True)
                    stmt = "select * from criminal where Criminal_name=%s"
                    my_cursor2.execute(stmt, (j, ))
                    for m in my_cursor2:
                        a = m[0]
                        print(m[0])
                        b = m[1]
                        print(m[1])
                        c = m[3]
                        print(m[3])
                        d = m[5]
                        print(m[5])
                        e = m[6]
                        print(m[6])
                        f = m[7]
                        print(m[7])
                        g = m[8]
                        print(m[8])
                        h = m[9]
                        print(m[9])
                        p = m[10]
                        print(m[10])
                        q = m[11]
                        print(m[11])
                        r = m[12]
                        print(m[12])
                        s = m[13]
                        print(m[13])
                    conn.commit()
                    my_cursor2.close()
                    conn.close()

    # Database connectivity and email sending...............

                    conn = mysql.connector.connect(
                        host='localhost', user='root', password='root', database='management')
                    my_cursor = conn.cursor()  # police
                    my_cursor.execute(
                        f"select Email from police where Area='{e}'")
                    receiver_email = ""
                    for i in my_cursor:
                        print(i)
                        receiver_email = i
                    print(receiver_email)
                    conn.commit()
                    my_cursor.close()
                    conn.close()

                    sender_email = "pjenil1609@gmail.com"
                    password = "xfngdsvjyzpirboj"
                    # message = f"""\
                    # Subject: Criminal Detected

                    # Details :

                    # Cam : {z}
                    # Name : {j}
                    # Location : {k}
                    # Criminal Id : {a}
                    # Criminal No : {b}
                    # Nick Name : {c}
                    # Age : {f}
                    # Occupation : {g}
                    # Birthmark : {h}
                    # Gender : {q}"""

                    message = EmailMessage()
                    sender = "pjenil1609@gmail.com"

                    message['From'] = sender
                    message['To'] = receiver_email
                    message['Subject'] = 'Criminal Detected !'
                    body = f"""Subject: Criminal Detected !

                    Details : 
                    
                    Cam : {z} 
                    Name : {j} 
                    Location : {k}
                    Criminal Id : {a}
                    Criminal No : {b}
                    Nick Name : {c}
                    Age : {f}
                    Occupation : {g}
                    Birthmark : {h}
                    Gender : {r}"""
                    message.set_content(body)
                    mime_type, _ = mimetypes.guess_type(f'{j}.jpg')
                    mime_type, mime_subtype = mime_type.split('/')
                    with open(f'./photos{j}.jpg', 'rb') as file:
                        message.add_attachment(file.read(),
                                               maintype=mime_type,
                                               subtype=mime_subtype,
                                               filename=f'{j}.jpg')
                    print(message)
                    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
                    mail_server.set_debuglevel(1)
                    mail_server.login("pjenil1609@gmail.com",
                                      'xfngdsvjyzpirboj')
                    mail_server.send_message(message)
                    mail_server.quit()
                    print("Mail Sent")

                    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
