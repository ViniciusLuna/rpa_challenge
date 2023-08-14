from selenium import webdriver
from time import sleep
import json

params = None

with open( './desenvolvimento.json', 'r' ) as p:
    params = json.loads( p.read() )

navegador = webdriver.Chrome()

navegador.get( params["url"] )

#sleep(5)
#Start
navegador.find_element('xpath', '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
sleep(5)