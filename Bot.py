import smtplib
import sqlite3


class Bot(object):
    def __init__(self):
        pass

    def mail_with_error(self, error: str): #отправляет мейл с ошибкой
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        smtpObj.login('botforerror@mail.ru','12345bot')
        smtpObj.sendmail("botforerror@mail.ru","kotlyarow1999@mail.ru",str(error))
        smtpObj.quit()
    def BD(self, operation: str, coin: str,amount: float,date: str):
        conn = sqlite3.connect("history.db")
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO history VALUES (?,?,?,?)", [(operation, coin, amount, date)])
        conn.commit()

        conn.close()

