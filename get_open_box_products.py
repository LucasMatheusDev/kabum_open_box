import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from models.open_box_product import OpenBoxProduct
from models.product import Product
from models.send_email import SendEmailInfo
from models.user import User
from send_email import send_email


def get_open_box_products(user: User, send_email_info: SendEmailInfo):
    print("Iniciando o navegador")
    # Iniciando o navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 1-  Acessar o site (www.kabum.com.br/login) da Kabuum na tela de login
    browser.get("https://www.kabum.com.br/login")

    # 2 - Preencher o login e senha e clicar em entrar
    username = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div/div[1]/div/div/input')
    password = browser.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div/div[2]/div/div/input')
    username.send_keys(user.kabum_email)
    password.send_keys(user.kabum_password)
    browser.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/div/button').click()

    # 3 Aguardando a tela carregar
    time.sleep(3)

    # 4 Apertando ESC para fechar o modal de promoção
    try:
        browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)

    except:
        pass

    # 5 - acessar produtos favoritos pelo link (https://www.kabum.com.br/minha-conta/favoritos)
    browser.get("https://www.kabum.com.br/minha-conta/favoritos")

    time.sleep(5)

    products: list[Product] = []

    open_box_products: list[OpenBoxProduct] = []

    # Pegando todos os produtos favoritos
    favoritesProducts = browser.find_elements(By.CLASS_NAME, "LIbqj")

    # Para cada produto favorito, criar um objeto do tipo Product
    for product in favoritesProducts:
        # pegar o link da imagem , pois o código do produto está na url da imagem
        productImageLink = product.find_element(By.CSS_SELECTOR, '.productImage').get_attribute('src')
        productCode = productImageLink.split('fotos/')[1].split('/')[0].strip()

        name = product.find_element(By.CSS_SELECTOR, '.productInfo h1').text

        link = f'https://www.kabum.com.br/produto/{productCode}/{name}'

        products.append(Product(productCode, name, link))

    # Para cada produto favorito, acessar o link do produto e verificar se existe um Open Box disponível
    for OpenBox in products:
        try:
            browser.get(OpenBox.link)

            # Aguardando a tela carregar pois o botão open box demora um pouco para aparecer
            time.sleep(5)

            # Se existir, pegar o valor do produto e o valor do open box
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
            browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(3)
            button_open_box = browser.find_element(By.CLASS_NAME, "iLGgzc")
            button_open_box.click()

            time.sleep(2)

            prices = []
            open_box_prices = browser.find_elements(By.CLASS_NAME, 'productPrice')
            if len(open_box_prices) > 0:
                for open_box_price in open_box_prices:
                    prices.append(open_box_price.text)

                open_box_products.append(OpenBoxProduct(OpenBox.name, str(prices), OpenBox.link))

        except:
            pass

    # Enviando email com os produtos open box
    if len(open_box_products) > 0:
        send_email(open_box_products, send_email_info)
    else:
        print("Não há produtos open box disponíveis")

    # Fechando o navegador
    browser.quit()
