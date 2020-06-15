from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

def click(xpath):
    driver.find_element_by_xpath(xpath).click()

def post(xpath, send):
    global mBox
    mBox = driver.find_element_by_xpath(xpath)
    mBox.send_keys(send)

def borrarSeguidos(usuario, contrasenia):

    #----------------------------------- abrir insta y hacer login
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')   
    time.sleep(1 + random.random())
    post('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input',
    usuario) #pone usuario    
    post('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input',
     contrasenia) #pone contraseña
    click('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div') #click para ingresar
    time.sleep(2 + random.random())

#----------------------------------- busca seguidores y los deja de seguir
    try:
        time.sleep(1 + random.random()) 
        click('/html/body/div[4]/div/div/div[3]/button[2]') #click en box de buscar
        time.sleep(random.random())       
        click('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img') #ir a usuario
        time.sleep(1+ random.random())
        
        click('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span') #ir a seguidos
        time.sleep(1+ random.random())

        for i in range(1,11):
            click('/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(i)) #click en seguido
            time.sleep(1+2*random.random())
            click('/html/body/div[5]/div/div/div[3]/button[1]') #deja de seguir
            time.sleep(1+2*random.random())

        click('/html/body/div[4]/div/div[1]/div/div[2]/button/svg/path') #cierro vent seguidos
        driver.close() #cierro chrome
    except:            
        driver.close()
     

usuario1 = "natibir.fashion"
contrasenia1 = "animal02"
usuario2 = "natalia.fitness.arg"
contrasenia2 = "modelnat01"

for i in range(1,10):
    borrarSeguidos(usuario2, contrasenia2)
    borrarSeguidos(usuario1, contrasenia1)    
    time.sleep(30 + random.random()) 
   
    
                                  
                                 
