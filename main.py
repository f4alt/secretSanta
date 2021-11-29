import config
import createConnections
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    for participant in createConnections.participants:
        # format email
        body = "SHHHH, you have " + participant.secretSanta + '''!
        Please remember to keep gifts around $150 max
        Looking forward to seeing everyone!'''
        subject = "Family Secret Santa 2021"

        msg = MIMEMultipart()
        msg['To'] = participant.email
        msg['From'] = config.gmail_user
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        message = msg.as_string()

        try:
            # send emails
            server = smtplib.SMTP(config.mailFromServer)
            server.starttls()
            server.login(config.gmail_user, config.gmail_password)

            server.sendmail(config.gmail_user, participant.email, message)
            server.quit()

            # write connections to log incase of email error, or people forget
            f = open('log.txt', 'a')
            f.write(participant.name + " has " + participant.secretSanta + "\n")
            f.close()

            # console confirmation
            print("Email Sent!")
        except:
            # print sending error to console
            print("Email Sending Error:", participant.email)

if __name__ == "__main__":
    main()
