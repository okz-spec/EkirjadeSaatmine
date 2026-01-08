from smtplib import SMTP_SSL
from email.message import EmailMessage

def saada_kiri(kellele, kellelt):
    server = "smtp.gmail.com"
    port = 465
    parool = "oqbm yqbi xcol ougl"

    kiri = EmailMessage()
    kiri["From"] = kellelt
    kiri["To"] = kellele
    kiri["Subject"] = "E-Kiri"

    fail = open("kiri.html", "r", encoding="utf-8")
    html_sisu = fail.read()
    fail.close()

    kiri.add_alternative(html_sisu, subtype="html")

    pilt = open("pilt.png", "rb")
    kiri.get_payload()[0].add_related(
        pilt.read(),
        maintype="image",
        subtype="png",
        cid="pilt"
    )
    pilt.close()

    try:
        with SMTP_SSL(server, port) as smtp:
            smtp.login(kellelt, parool)
            smtp.send_message(kiri)
            print("Kiri saadetud")
    except Exception as e:
        print(f"Midagi läks valesti ...{e}")

saada_kiri("marat.matvejev@mail.ee", "maratmatveev1337@gmail.com")