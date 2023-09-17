import time

from fibonacci import fibonacci_generator

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

piano_link = 'https://www.musicca.com/piano'
driver.get(piano_link)

SCALE_TO_CSS_SELECTOR = {
        '0': '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[2]/span[2]',
        '1': '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[3]/span',
        '2':       '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[4]/span[2]',
        '3' :               '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[5]/span[2]',
        '4':       '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[6]/span[1]',
        '5' :                        '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[7]/span',
        '6'   :   '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[8]/span[2]',
        '7'  :     '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[9]/span[2]',
        '8' :     '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[10]/span',
        '9':       '/html/body/div[2]/div/div/div/div/div[2]/article/div[2]/div/div[1]/div[2]/ul/li[11]/span[2]',





}

def play(fib_term, driver):
    for digit in str(fib_term):
        key = driver.find_element(By.XPATH, SCALE_TO_CSS_SELECTOR[digit])
        key.click()
        time.sleep(0.2)

for term in fibonacci_generator():
    play(term, driver)
