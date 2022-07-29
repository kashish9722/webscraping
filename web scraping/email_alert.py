import smtplib
from email.message import EmailMessage

def alert_system(product, link):
    email_id = 'kashishsingla48@gmail.com'
    email_pass = 'jhenbffemhlswbhx'


    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'kashishsingla1212@gmail.com' # receiver address
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)