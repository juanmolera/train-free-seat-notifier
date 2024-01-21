import smtplib, ssl
import os
from dotenv import load_dotenv
import re

load_dotenv()

password = os.getenv('password')

pattern = r'([^@]+)'

def send_confirmation_email(email, date, time):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "trainfreeseatnotifier@gmail.com"
    receiver_email = email
    receiver_email = "trainfreeseatnotifier+person1@gmail.com"

    name = re.match(pattern, sender_email)[0]

    message = f"""\
    Subject: Se ha creado una alerta de plazas libres para un trayecto en tren 

    Hola {name},

    -----------------------------------------------------------------------

    Detalles del viaje:

    ORIGEN-DESTINO

    FECHA: {date}

    HORA DE SALIDA: {time}

    -----------------------------------------------------------------------

    No responda a este correo, es un mensaje automatico de la app de avisos de plazas en trenes."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def send_alert_email(email, date, time):

    pass