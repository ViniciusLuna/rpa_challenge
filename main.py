from selenium import webdriver
from time import sleep
import json

params = None

with open( './desenvolvimento.json', 'r' ) as p:
    params = json.loads( p.read() )

navegador = webdriver.Chrome()

navegador.get( params["url"] )

sleep(5)