from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import datetime
mensagem = 'Ola'
a = datetime.datetime.now()
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe", options=chrome_options)
driver.set_page_load_timeout(80)
for x in range(1):
    driver.get('https://meu.site.com/')
    driver.find_element_by_name('nome').send_keys('Usuario')
    driver.find_element_by_name('email').send_keys('insatisfeito.com.o.seu.servico@gmail.com')
    assunto = Select(driver.find_element_by_name('assunto'))
    assunto.select_by_visible_text('Críticas, Sugestões ou Elogios')
    driver.find_element_by_name('mensagem').send_keys(mensagem)
    driver.find_element_by_id('enviar').click()
    WebDriverWait(driver, 50).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#wpcf7-f146-p75-o1 > form > div.wpcf7-response-output.wpcf7-display-none.wpcf7-mail-sent-ok")))
    assert 'Sua mensagem foi enviada' in driver.page_source
    print('Envio de nummero', x+1 ,' as ',a.strftime("%H:%M:%S %d/%m/%Y"))
    driver.implicitly_wait(1)
driver.quit()
