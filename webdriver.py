from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

url = 'http://g1.globo.com'

# driver = webdriver.Remote(
#    command_executor='http://172.22.5.44:5555/wd/hub',
#    desired_capabilities={
#        'browserName': 'firefox',
#        'version': '36.0'})

_exe_binary = FirefoxBinary(r'C:\_dev_\Firefox36\firefox.exe')
_exe_driver = "C:\\_dev_\\_selenium\\firefox\\geckodriver.exe"
#
# # fp = (r'C:\Users\000164\AppData\Roaming\Mozilla\Firefox\Profiles\q984rkzo.teste')
# # opts = Options()
# # opts.profile = fp
#
# _firefox_capabilities = DesiredCapabilities.FIREFOX
# _firefox_capabilities['marionette'] = False
#
# # COLOCA AQUI DENTRO O CAPABILITIES,
# # O PATH DO DRIVER E O BINARIO FX36
# driver = webdriver.Firefox(executable_path="C:\\_dev_\\_selenium\\firefox\\geckodriver.exe", firefox_binary=_exe_binary, desired_capabilities=_firefox_capabilities, options=options)
# # driver = webdriver.Firefox(executable_path="C:\\_dev_\\_selenium\\firefox\\geckodriver.exe", options=options)
# # driver.maximize_window()
# # driver.set_page_load_timeout(60)

fp = (r'C:\Users\000164\AppData\Roaming\Mozilla\Firefox\Profiles\q984rkzo.teste')
opts = Options()
opts.profile = fp
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = False
driver = webdriver.Firefox(capabilities=firefox_capabilities, firefox_binary=_exe_binary, firefox_profile=fp)

# driver = webdriver.Chrome(executable_path=r"C:\_dev_\_selenium\chrome\chromedriver.exe")

driver.get("https://www.mozilla.org/en-US/foundation/documents")
driver.find_element(By.CSS_SELECTOR, ".rich-text > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, ".rich-text > ul:nth-child(19) > li:nth-child(2) > a:nth-child(1)").click()

# Disponíveis em: http://kb.mozillazine.org/About:config_Entries
p = FirefoxProfile()

# Configurações para download
# p.set_preference("browser.download.manager.showAlertOnComplete", False) ok
# p.set_preference("browser.download.panel.shown", False) ok
p.set_preference("browser.shell.checkDefaultBrowser", False)
p.set_preference("browser.download.folderList", 0)
p.set_preference("browser.download.manager.showWhenStarting", False)
p.set_preference("browser.download.manager.alertOnEXEOpen", False)
# Só downloads PDF
p.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
# p.set_preference("browser.download.importedFromSqlite", False) ok
# p.set_preference("pdfjs.disabled", True) ok
# p.set_preference("pdfjs.showPreviousViewOnLoad", False) ok
# p.set_preference("pdfjs.previousHandler.preferredAction", 4) ok
# p.set_preference("pdfjs.previousHandler.alwaysAskBeforeHandling", True)
p.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
p.set_preference("pdfjs.migrationVersion", 2)

#Configurações Câmera e audio
# p.set_preference("media.webspeech.recognition.enable", True)
p.set_preference("camera.control.face_detection.enabled", True)
p.set_preference("dom.imagecapture.enabled", True)

  # Limpa cache e cookies
  p.set_preference('browser.cache.disk.enable', False)
  p.set_preference('browser.cache.memory.enable', False)
  p.set_preference('browser.cache.offline.enable', False)
  p.set_preference('network.cookie.cookieBehavior', 2)

p.update_preferences() #Provavelmente aplica


driver = webdriver.Firefox(firefox_binary="caminho/firefox36", firefox_profile=pp)
