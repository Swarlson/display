# -*- coding: utf-8 -*-
from time import sleep, strftime, localtime
from I2C_LCD_driver import lcd
import urllib.request

#Todo: Mach active/testing main methods damit du nicht ständig den ganzen shit rauskommentieren musst
#Todo: Do binance implementation (maybe other project for this) calls etc zu simulieren und zu schauen wie es läuft

investment = 393.21
n_coins = 322
content = "Foobar"
failed_requests = 0

def evaluate_patrik(rate, investment, n_coins):
    dif = round(float(rate)*n_coins - investment, 2)
    if dif < 0:
        content = pepelaugh(dif)
    else:
        content = pogChamp(dif)

    return content


def pepelaugh(dif):
    content = ("KEKW ->{} EUR".format(dif))
    print(content)
    return content

def pogChamp(dif):
    content = ("Pog->{} EUR".format(dif))
    print(content)
    return content

if __name__ == "__main__":
    mylcd = lcd()
    mylcd.screens = range(0,1)
    mylcd.start()
    #resp = msg.request_only_price('enjincoin', 'eur')
    #evaluate_patrik(resp,investment,n_coins)
    try:
        while True:
            clocktime = strftime('%H:%M:%S',localtime())
            time_display = "Updated " + clocktime
            ip_display = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
            mylcd.update_buffer(time_display,1,0)
            mylcd.update_buffer(ip_display,2,0)
            sleep(60) 
    except KeyboardInterrupt:
        print('Ending the program')

    