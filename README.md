# Open Box Kabum 

## O que é?

A loja [Kabum](kabum.com.br) oferece produtos OpenBox, os OpenBox são produtos novos ou seminovos que retornaram ao KaBuM!, uma vez retirados de suas caixas originais, ganham o status de reembalados, classificação “Excelente” ou “Muito Bom”, além de um desconto bem especial.

Para saber mais sobre o OpenBox, acesse o site da Kabum: https://www.kabum.com.br/openbox/

## Qual é o papel deste software?
Este software tem como objetivo facilitar a compra de produtos mais baratos na loja virtual da [Kabum](kabum.com.br), através de um script que faz a busca de produtos com base na sua lista de **favoritos** e caso tenha algum produto openBox, voce recebe um e-mail com uma lista desses produtos.

## Como Usar?

A utilizacao do software e bem simples,tudo que você precisa fazer é definir as variaveis do arquivo **[main.py](main.py)** e executar o script.

### Exemplo de variaveis (Arquivo main.py)


```python
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

# o smtp server depende do email de envio que voce escolher :
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

```


Agora rode o Script e pronto você ja esta recebendo os produtos openBox da Kabum.


## Aprimoramentos

Você tem total liberdade para clonar este software e salva-lo em seu servidor, para que ele rode 24 horas por dia, e assim voce sempre esteja recebendo os produtos openBox da Kabum.

