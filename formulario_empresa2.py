from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import datetime
from gerador import RF
from random import randint
rg = RF()
oi = rg.set_rg()
tel = rg.set_numero()
mensagem = 'mensagem aqui'
a = datetime.datetime.now()
hoje = a.strftime("%d%m%Y")
hora = ['1800', '1000', '0900', '1700', '1930', '1845']
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)
driver.set_page_load_timeout(80)
for x in range(5000):
    driver.get('site3.com.br')
    driver.find_element_by_name('nome').send_keys('Usuario')
    driver.find_element_by_name('rg').send_keys(oi)
    driver.find_element_by_name('telefone').send_keys(tel)
    driver.find_element_by_name('data').send_keys(hoje)
    driver.find_element_by_name('horario').send_keys(hora[randint(0,5)])
    driver.find_element_by_name('local').send_keys('lalala')
    driver.find_element_by_name('mensagem').send_keys(mensagem)
    driver.find_element_by_class_name('btEnviar').click()
    WebDriverWait(driver, 50).until(expected_conditions.alert_is_present())
    alerta = driver.switch_to_alert()
    alerta.accept()
    print('Envio de nummero', x+1 ,' as ',a.strftime("%H:%M:%S %d/%m/%Y"))
    driver.implicitly_wait(1)
driver.quit()