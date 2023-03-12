import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models.open_box_product import OpenBoxProduct
from models.send_email import SendEmailInfo


def send_email(open_box_products: list[OpenBoxProduct], send_email_info: SendEmailInfo):
    number_of_errors = 0
    try:
        # # Converte a lista de produtos para uma string
        products_str = ''
        for open_box_product in open_box_products:
            products_str += f"Produto: {open_box_product.name}\n Preços: {open_box_product.prices.replace(',', '')}\n Link: {open_box_product.link}\n\n"
        print(f'produtos encontrados: {products_str}')

        # Cria a mensagem a ser enviada
        body_message = f"Lista de produtos Open Box disponiveis:\n{products_str}"
        message = MIMEMultipart()

        message["From"] = send_email_info.email_from
        message["To"] = send_email_info.email_to
        message["Subject"] = "Lista de Produtos Open Box"
        message.attach(MIMEText(body_message, "plain"))

        with smtplib.SMTP(send_email_info.smtp_server, port=send_email_info.smtp_port) as connection:
            connection.starttls()
            connection.login(user=send_email_info.email_from, password=send_email_info.email_password)
            connection.sendmail(from_addr=message['From'], to_addrs=message['To'], msg=message.as_bytes())
            connection.close()
            print("Email enviado com sucesso")

    except Exception as e:
        if number_of_errors < 3:
            number_of_errors += 1
            send_email(open_box_products, send_email_info)
        print("Exception quando enviar o email: ", e)


    except:
        print("Erro ao enviar o email")
