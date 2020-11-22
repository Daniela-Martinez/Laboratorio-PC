#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

data = {}
#with open('pass.json') as f:
#    data = json.load(f)
#create message object instance
msg = MIMEMultipart()
message = 'Hola es una prueba de tarea'
msg['From'] = 'daniela.martinezrdr@uanl.edu.mx'
receipents=['d.rdz.240615@gmail.com', 'armtzmtz@live.com', 'fernandalealmo@uanl.edu.mx', 'd_a_n_y_722@gmail.com']
msg['To'] = ', '.join(receipents)
msg['Subject'] = "PruebaLab"
msg.attach(MIMEText(message, 'plain'))
#create server
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()
# Login Credentials for sending the mail
server.login('daniela.martinezrdr@uanl.edu.mx', 'SoMA3PRT')
server.sendmail( msg['From'], receipents, msg.as_string())
print('successfully sent email to %s:' % (msg['To']))   
server.quit()  
