import config
import createConnections
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    for participant in createConnections.participants:
        body = "SHHHH, you have " + participant.secretSanta + " :)"
        subject = "Secret Santa"

        msg = MIMEMultipart()
        msg['To'] = participant.email
        msg['From'] = config.gmail_user
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        message = msg.as_string()

        try:
            server = smtplib.SMTP(config.mailFromServer)
            server.starttls()
            server.login(config.gmail_user, config.gmail_password)

            # sendmail(from, to, message)
            server.sendmail(config.gmail_user, participant.email, message)
            server.quit()

            print("Email Sent!")
        except:
            print("Email Sending Error")

if __name__ == "__main__":
    main()
