import time
from lib2to3.pgen2 import driver

import form as form
from behave import given, when, then
from selenium import*
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given(u'que acesso o site Petz')
def step_impl(context):
    context.driver.get('https://www.petz.com.br/')
    print('Passo 1 - Acessou no site Petz')
    time.sleep(2)  # espera bruta



@given(u'Clico no botao aceito politica de privacidade')
def step_impl(context):
    print('Passo 2 - Clicou no botaão aceito politica de privacidade')
    context.driver.find_element(By.ID, 'aceiteLgpd').click()
    time.sleep(4)

@then(u'clico no texbox de pesquisa')
def step_impl(context):
    print('Passo 3 - clicou no texbox de pesquisa')
    context.driver.find_element(By.ID,'search').click()
    time.sleep(4)

@then(u'limpo o campo')
def step_impl(context):
    print('Passo 4 - limpou o campo de pesquisa')
    context.driver.find_element(By.ID, 'search').clear()
    time.sleep(4)

@then(u'digito o nome do produto "Biscoito Golden Cookie para Cães Adultos 350g"')
def step_impl(context):
    print('Passo 5 -digitou o nome do procuto Biscoito Golden Cookie para Cães Adultos 350g')
    context.driver.find_element(By.ID, 'search').send_keys('Biscoito Golden Cookie para Cães Adultos 350g')
    time.sleep(15)

@then(u'clico no enter')
def step_impl(context):
    print('Passo 6 - Clicou enter')
    context.driver.find_element(By.ID, 'search').send_keys(keys.Keys.ENTER)

@when(u'clico no botao adcionar ao carrinho')
def step_impl(context):
    print('Passo 7 - clicou no botao adcionar ao carrinho')
    #context.driver.find_element(By.ID, 'adicionarAoCarrinho').click()
    #context.driver.find_element(By.XPATH, '/ html[1] / body[1] / div[9] / main[1] / div[1] / div[1] / div[1] / div[2] / div[11] / button[1]').click()
    #time.sleep(30)
    #context.driver.find_element(By.XPATH,'/html[1]/body[1]/div[9]/main[1]/div[1]/div[1]/div[1]/div[2]/div[3]').click()
    print('Passo 7.1 - clicou no botao adcionar ao carrinho')

'''
@then(u'valido se o produto confere')
def step_impl(context):
    print('Passo 8 - Validou se o produto confere')
    print(context.driver)
    context.driver.find_element(By.XPATH,'/html[1]/body[1]/div[9]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h1[1]')
    #assert context.driver.find_element(By.CSS_SELECTOR,'div.site-wrap:nth-child(37) main.container-produto:nth-child(5) div.container.interna div.row.desktop-margin:nth-child(8) div.productTemplate.center-image div.col-xs-12.col-sm-6.col-md-6:nth-child(4) div.product-title:nth-child(1) > h1:nth-child(1)').text == 'Biscoito Golden Cookie para Cães Adultos 350g'




@then(u'valido se o preco e igual ao informado na pagina de pesquisa')
def step_impl(context):
    print('Passo 9 - Validou sebhe o preco é igual ao informado na pagina de pesquisa')


@given(u'digito o nome do produto "Biscoito Golden Cookie para Cães Adultos 350g"')
def step_impl(context):
    print('Passo 2c -Digitou o nome do produto ')
'''