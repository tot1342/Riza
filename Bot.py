import smtplib

class Bot(object):
    def __init__(self):
        pass

    def mail_with_error(self, error: str):
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        smtpObj.login('botforerror@mail.ru','12345bot')
        smtpObj.sendmail("botforerror@mail.ru","kotlyarow1999@mail.ru",str(error))
        smtpObj.quit()
