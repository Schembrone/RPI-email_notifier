#rpi mail notifier
from gpiozero import LED
from time import sleep
from imapclient import IMAPClient

USERNAME = 'your_email_username'          # the username of your email account
PASSWORD = 'your_email_password'          # the password of your email account
MAIL_OFFSET = 0                           # the number of unread emails in your inbox to ignore
HOST = 'imap.host.com'                   # your IMAP server in the form "imap.host.com"
LED_PIN = 21                              # the GPIO pin that you want to use to control the LED

def check():
    led = LED(LED_PIN)
    server = IMAPClient(HOST, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    folder = server.select_folder("INBOX", readonly=True)
    unread_count = len(server.search("UNSEEN"))

    if unread_count > MAIL_OFFSET:
        led.on()
    else:
        led.off()

    server.logout()
    sleep(10)

while True:
    check()