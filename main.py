from selenium import webdriver
from selenium.webdriver.common.by import By


import time

driver = webdriver.Firefox()

driver.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiG_6uRpOv0AhVBVTABHX6xAugQFnoECAUQAQ&url=https%3A%2F%2Felpais.com%2Fnoticias%2Fpetroleo%2F&usg=AOvVaw0PPpshcESPDoCl2yaQFVbH')
driver.maximize_window()

try:
    boton_cookies = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
    boton_cookies.click()
    time.sleep(2)
except Exception as e:
    print(f'El boton de cookies no existe: {e}')
    pass

contenedor_noticias = driver.find_element(By.CLASS_NAME, "b-au_b")
noticias = contenedor_noticias.find_elements(By.TAG_NAME, 'article')

for noticia in noticias:
    header_noticia = noticia.find_element(By.TAG_NAME, 'header')
    enlace_noticia = noticia.find_elements(By.TAG_NAME, 'a')
    print(enlace_noticia[1].get_attribute('innerHTML'))
