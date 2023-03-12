import functools

from get_open_box_products import get_open_box_products
from models.send_email import SendEmailInfo
from models.user import User
from search_schedule import search_schedule





# seu email da kabum
kabum_email: str = "example@hotmail.com"

# sua senha da kabum
kabum_password: str = "example***"

# A lista de horarios que as buscas serao feitas
hours_to_search: list = ['11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', ]

# quem ira enviar o email com o produtos
email_from: str = "example@hotmail.com"

# senha do email 
email_password: str = "example***"

# Email de quem recebe as listas de produtos
email_to: str = "example@gmail.com"

# o smtp server depende do email que voce escolher :
# Gmail: smtp.gmail.com
# Outlook: smtp-mail.outlook.com
# Yahoo: smtp.mail.yahoo.com
# Hotmail: smtp.live.com
# Office 365: smtp.office365.com
smtp_server = "smtp.office365.com"

# a porta do smtp server depende do email que voce escolher :
# Gmail: 465
# Outlook: 587
# Yahoo: 465
smtp_port = 587

send_email_info = SendEmailInfo(email_from, email_password, email_to, smtp_server, smtp_port)

user = User(kabum_email, kabum_password)


if __name__ == '__main__':
    search_schedule(functools.partial(get_open_box_products, user, send_email_info), hours_to_search)
