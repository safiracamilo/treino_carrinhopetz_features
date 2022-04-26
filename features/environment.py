from selenium import webdriver

# Início
def before_all(context):    # Antes de Tudo
    # Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/PHILCO/PycharmProjects/treino_carrinhopetz_features/drives/chrome96/chromedriver.exe')

    context.driver.maximize_window()
    context.driver.implicitly_wait(30)

    print('Passou A - Antes de Tudo')

# Fim
def after_all(context):     # Depois de Tudo
    # Desligar / Detruir o objeto do Selenium
    context.driver.quit()

    print('Passou Z - Antes de  tudo')

def after_step(contex, step):
    print()
