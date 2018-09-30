import smtplib
from time import sleep

LOG_EMAIL, LOG_PSW = "botforerror@mail.ru", "12345bot"
GENERAL_EMAILS = ["kotlyarow1999@mail.ru", "celestial.vultures@gmail.com"]

class ConnectionFailed():
    def __init__(self, method, message, args: dict, err_time):
        '''
        Recall ::method:: with ::args:: but new ::err_time:: and,
        if err_time is large enough log the ::message:: info file and email
        '''
        self.method = method
        self.message = message
        self.args = args
        self.args[err_time] = err_time

    def log(self): # TODO: txt/log output
        if exp(err_time) > 145:
            # Sending email with error to our .log. email adresses
            smtpObj = smtplib.SMTP('smtp.mail.ru', LOG_PSW)
            smtpObj.starttls()
            smtpObj.login(LOG_EMAIL, LOG_PSW)
            smtpObj.sendmail(LOG_EMAIL, LOG_EMAIL, self.message)
            smtpObj.quit()

        if exp(err_time) > 3600:
            # Sending email with error to our .general. email adresses
            smtpObj = smtplib.SMTP('smtp.mail.ru', LOG_PSW)
            smtpObj.starttls()
            smtpObj.login(LOG_EMAIL, LOG_PSW)
            for genmail in GENERAL_EMAILS:
                smtpObj.sendmail(LOG_EMAIL, genmail, self.message)
            smtpObj.quit()

    def repeat(self, method=self.method):
        # Recall method after exp(t) sec waiting the normal connection
        sleep(exp(err_time))
        self.method(**self.args)
