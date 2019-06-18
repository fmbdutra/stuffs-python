# coding: latin-1

import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
envia_email = "meu_email@email.com"
recebe_email = ['email_1@a.com', 'email_n@a.com']
assunto = 'coloque_assunto_aqui'
file_location = r"_coloque_o_caminho_completo_do_arquivo\\arquivo.ext"

raiz_email = MIMEMultipart('mixed')
# raiz_email = MIMEMultipart('related')
raiz_email['From'] = assunto
para = ''
# Aqui um FOR para ele criar única string para todos os envios
for c in recebe_email:
    para += c + ';'
      
raiz_email['To'] = para
raiz_email['Subject'] = assunto
# raiz_email.preamble = 'This is a multi-part message in MIME format.'

html = """\
mensagem em html <b>aqui</b><br>
E uma imagem<br><img src="cid:image1"><br>
"""
parte = MIMEText(html, 'html')

raiz_email.attach(parte)

# Configura anexo
def_anexo = os.path.basename(file_location)
abre_arquivo = open(file_location, "rb")
anexo = MIMEBase('application', 'octet-stream')
anexo.set_payload(abre_arquivo.read())
encoders.encode_base64(anexo)
anexo.add_header('Content-Disposition', "attachment; filename= %s" % def_anexo)

# Coloca o anexo no MIMEMultipart
raiz_email.attach(anexo)

try:
   # Descomentar linha abaixo
   smtp_obj = smtplib.SMTP('email.server.com:25')
   smtp_obj.sendmail(envia_email, recebe_email, raiz_email.as_string())
   print("Enviado com sucesso")
except smtplib.SMTPException:
   print("Erro: não deu certo")
