import smtplib

sender = 'oi@oi.com'
receivers = ['tchau@tchau.com']

message = """From: Eu <"""+sender+""">
To: Alguem <alguem@provedor.com>
Subject: Teste Python

Hello World Email Python
"""

try:
   # Descomentar linha abaixo
   # smtpObj = smtplib.SMTP('rede.interna:25')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")