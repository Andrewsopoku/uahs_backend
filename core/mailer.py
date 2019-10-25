
__author__ = 'andrews'

import requests
import smtplib
from email.mime.text import MIMEText

class Mailer(object):
    def __init__(self):

        self.api_key = 'key-71308276fd92f3dc2c0e984748126593'
        self.domain = 'sandbox0c10cb96cc7b47b28614888ea25d8a5f.mailgun.org'

        self.url = 'https://api.mailgun.net/v3/{}/messages'.format(self.domain)

    def send_message(self, subject, message, to, sender):
         #self.domain = 'www.taxstamps.com'
         return requests.post(
         self.url,
         verify=False,
         auth=("api", self.api_key),
         data={"from": sender,
         "to": to,
         "subject": subject,
         "html": message})

    def send_via_smtp(self, subject, message, to):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "hello@goldkeys.net"
        msg['To'] = to
        s = smtplib.SMTP('smtp.mailgun.org', 587)
        s.login('postmaster@www.goldkeys.net', 'a09a61a6a4a4d1d083f5aaf30f83ddcd')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()