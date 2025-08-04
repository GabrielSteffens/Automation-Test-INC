from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver():
    options = webdriver.ChromeOptions()
    # Se quiser rodar sem abrir o navegador, ative o headless
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver
