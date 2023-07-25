<h3 align="center">RPI-email_notifier</h3>

<div align="center">

  [![GitHub Issues](https://img.shields.io/github/issues/Schembrone/RPI-email_notifier.svg)](https://github.com/Schembrone/RPI-email_notifier/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/Schembrone/RPI-email_notifier/pulls)
  [![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](/LICENSE)

</div>

---

<p align="center">This is an application based on a Raspberry Pi that uses a python script to control a LED. The purpose of this project is to visually indicate to the user the presence of unread messages in their email inbox.
    <br> 
</p>

## 📌 Table of Contents
- [How it works](#working)
- [Requirements](#requirements)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Customizations](#customizations)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🚀 How the Project Works <a name = "working"></a>

When the Python script `mail_notifier.py` is executed on the Raspberry Pi, it connects to the user's email inbox via the IMAP protocol. The script checks for unread messages and if there are (excluding those to be ignored based on the `MAIL_OFFSET` setting), the LED connected to a GPIO pin turns on to notify the user. Otherwise, the LED remains off.
The script runs in an infinite loop, checking for new emails, by default, every 10 seconds. As soon as the user reads or manages the unread emails the LED reflects the change.

## 📋  Requirements <a name = "requirements"></a>
- [ ] Raspberry Pi (tested on Raspberry Pi 3 Model B+ running Raspberry PI OS Lite 64-bit)
- [ ] LED and appropriate resistor
- [ ] Accessible email account with IMAP support
- [ ] Python 3.x and pip installed on the Raspberry Pi

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your RPI.

### Prerequisites
- Install Dependencies:
  ```
  pip install IMAPClient
  ```
- LED Configuration:
  Connect the LED to the Raspberry Pi, ensuring the use of an appropriate resistor.<br>
  
  WARNING! if you are not using [BCM](https://www.raspberrypi.com/documentation/computers/images/GPIO.png) pin 21 you need to modify line 10 in `mail_notifier.py`

### Installing
Clone this Repository to your RPI file system

```
git clone https://github.com/Schembrone/RPI-email_notifier.git
```
### Script set up
Open `mail_notifier.py` and modify the following variables with your information:
   ```python
   USERNAME = 'your_email_username'          # the username of your email account
   PASSWORD = 'your_email_password'          # the password of your email account
   HOST = 'imap.host.com'                    # your IMAP server in the form "imap.host.com"
   LED_PIN = 21                              # the GPIO pin that you want to use to control the LED
   ```

## ⚙️ Usage <a name = "usage"></a>

1. Ensure that the LED is correctly connected to the Raspberry Pi.

2. Run the Python script:
   ```
   python mail_notifier.py
   ```
## 🎨 Customizations <a name = "customizations"></a>

Feel free to experiment and tailor the project to meet your needs and create a personalized system using your RPI.
By design you can change some variables inside `mail_notifier.py` to adjust the code to your needs:

- **Check Interval**: If you wish to modify the time interval between email checks, you can change the value of the `sleep` function called in line 26. Adjusting the check interval allows you to control how frequently the program checks for new emails.

- **Mail Offset**: If you have some emails that you don't want to read or you just want to get notified after a certain amount of unread emails are collected, you can easily change the `MAIL_OFFSET` variable and set it to the number of emails that you want to ignore.

- **Mail Folder**: If you want to check for the presence of unread emails in other folders than the inbox, you may want to change the first parameter passed to the method `select_folder` called on line 17.


## ✍️ Authors <a name = "authors"></a>
- [@Schembrone](https://github.com/Schembrone) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
This project relies on the following dependencies:

- [gpiozero](https://gpiozero.readthedocs.io/): A simple interface to GPIO devices with Raspberry Pi.
- [IMAPClient](https://github.com/mjs/imapclient): A Python library to access and manipulate IMAP servers.
