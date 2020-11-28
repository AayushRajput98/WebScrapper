# WebScrapper
This is a small handy python application that can be used to keep track over certain products and their price and notify you via email when the price are lowered to your satisfaction.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requried dependencies.

```bash
$ pip install requests bs4
```

## Usage

You can get your user agent by searching 'My User-Agent' in google.

### Send Mail
To send mail via gmail ID, you can either use [GoogleLessSecure](https://myaccount.google.com/lesssecureapps) feature or set up a 2-step verification [link](https://www.google.com/landing/2step/).
After you have set up the 2-step verification generate an app(Mail/Windwos10) password [link](https://myaccount.google.com/apppasswords) which can be used to while sending the mail.

```python
server.login('mail.address01@gmail.com', 'password you get from above step')
    subject = '[SBOT]Notification: Price down for your desiered product.'
    body = "Check the link, " + URL
    msg = f"Subject: {subject}\n\n{body}" 
```

### Process Management
To set the program up so that you don't have to run it again and again you can add the following snippet to the code.

```python
while True:
    check_price()
    time.sleep(60*60*12) 
```
This will run the check_price() function every 12 hrs.


