# import necessary packages

# Habilitar email não seguro no gmail para aceitar uso de terceiros:
# Logar no Gmail no navegador
# Entrar nesse link: https://myaccount.google.com/lesssecureapps

# Depois, habilitar SMTP do gmail

import smtplib

to = 'para_quem@email.com'
user = 'seu_email@email.com'
pwd = 'sua_senha_email'

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(user, pwd)

header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:Teste Python \n'
print(header)
msg = header + '1, 2, 3\n Testando\nEi\nPython\nTestando \nHello World Python Email \n\nObrigado!'

smtpserver.sendmail(user, to, msg)
print('Feito!')
smtpserver.close()
