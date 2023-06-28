from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Edge()

url = 'http://localhost:3000'

navegador.get(url)

sleep(3)

loginButton = navegador.find_element(By.ID, "google-btn")
loginButton.click()

sleep(3)

emailcampo = navegador.find_element(By.ID, "identifierId")
emailcampo.send_keys("herbert.silva60@aluno.ifce.edu.br",Keys.ENTER)

sleep(3)

senha = navegador.find_element(By.XPATH,'//*[@type = "password"]')
#senha.click()
senha.send_keys("Aae22032005#", Keys.ENTER)
#navegador.find_element(By.TAG_NAME, "avançar").click()


variavel = input()