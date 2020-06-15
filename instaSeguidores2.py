from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import sqlite3

def click(xpath):
    driver.find_element_by_xpath(xpath).click()

def post(xpath, send):
    global mBox
    mBox = driver.find_element_by_xpath(xpath)
    mBox.send_keys(send)


#def guardaSeguido(nombreSeguido):
    
    conexion1 = sqlite3.connect("base1")
    miCursor = conexion1.cursor()     
    
    miCursor.execute("""
        CREATE TABLE SEGUIDOS (
            CODIGOID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50))
            """)
    
    datos = str(content)
    print(content)
    miCursor.execute('INSERT INTO USUARIOS VALUES (?)', datos)
    #except: #sqlite3.OperationalError:     
        #print("error")    
        #pass
    #finally:
    conexion1.commit()
    conexion1.close()


def seguidor(usuario, contrasenia, listaTargets):

    #----------------------------------- abrir insta y hacer login
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')   
    time.sleep(2 + random.random())   
    post('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input', usuario) #pone usuario
    post('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input',
    contrasenia) #pone contraseña
    click('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div') #click para ingresar
    time.sleep(2 + random.random())
    click('//*[@id="react-root"]/section/main/div/div/div/div/button') #click para ahora no guardar
    time.sleep(1 + random.random())
    click('/html/body/div[4]/div/div/div/div[3]/button[2]') #activar notif ahora no
    time.sleep(1 + random.random())

    #----------------------------------- buscar personalidad    
    for i in range(1):
        conta = 0
        for target in listaTargets:    
            if conta >= 40:
                driver.close()
                break
            else:
                try:
                    time.sleep(1+random.random()) #cambie acaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                    try:                                        
                        post('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input', target) #pongo el target
                    except:
                        pass                    
                    try:
                        time.sleep(2+ random.random())
                        click('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span')
                    except:                                                                                 #da click al target
                        pass                    
                    try:
                        time.sleep(1+ random.random())
                        click('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a') #va a los seguidores
                        time.sleep(2 + random.random())       
                    except:
                        pass
                    for i in range(1,30):
                        try:
                            if conta >= 48:
                                driver.close()
                                break   
                            time.sleep(2 + random.random())  
                            nombreSeguido = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[1]/div[2]/div[1]/a').text    
                            guardaSeguido(nombreSeguido)                                     
                            time.sleep(1000 + random.random())  
                            click('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[2]/button'.format(i)) #pone seguir
                            conta += 1                                                 
                            time.sleep(1+ random.random())                              
                            try:                                
                                click('/html/body/div[5]/div/div/div/div[3]/button[2]') #cancela a dejar de seguir
                            except:                                
                                pass
                            time.sleep(random.random())
                            try:
                                click('/html/body/div[4]/div/div[1]/div/div[2]/button') 
                            except:
                                pass
                            time.sleep(1+ random.random())
                        except:
                            pass
                    try:
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()
                    except:
                        driver.close() 
                    time.sleep(1+ random.random())  

                except:
                    pass
                                   
                            

listaTargets1 = ['coderhouse', 'programacion_de_videojuegos', 'rocket_code' ]
#  voy 44 seguidos

#listaTargets1 = ["moria_laone", "alferdezok", "juliana.awada", "verolozanovl", "fulopcatherine", "mirthalegrand", 
#"cristinafkirchner","mauriciomacri", "cinthia_fernandez_", "lasobrideperez"]
listaTargets2 = ["candemolfese", "holasoylaurita", "wanda_icardi", "valentinazenere", "lalioficial", 
"antonelaroccuzzo", "tinistoessel", "pampitaoficial","nikitaneumannoficial", "jimenabaron.ok"] 
listaTargets3 = ["leomessi", "pvikinga", "darioorsi", "mauroicardi", "luisanalopilato", "franciscus", 
"marcelotinelli", "valentinazenere", "candelariatinelli", "orianasabatini"]
listaTargets4 = ["florivigna", "sangrejaponesa", "barbiepucheta", "gimeaccardi", "chavespauok", 
"juanittinelli1", "angelitatorresok", "kicillofok", "gimenezsuok", "marley_ok"]

arrayTargets = [listaTargets1]
#arrayTargets = [listaTargets2]
#arrayTargets = [listaTargets3]
#arrayTargets = [listaTargets4]
#arrayTargets = [listaTargets1, listaTargets2, listaTargets3, listaTargets4] #todas

usuario1 = "natibir.fashion"
contrasenia1 = "animal02"
usuario2 = "natalia.fitness.arg"
contrasenia2 = "modelnat01"
usuario3 = "tecyprog"
contrasenia3 = "Yaaaaa"

#time.sleep(5*3600 + 10*random.random()) #tiempo de inicio para cuando salgo
#tiempoLoops = 1200 #tiempre entre listas
tiempoLoops = 10

for j in range(1):
    
    try:
        for listaTargets in arrayTargets:
            #seguidor(usuario1, contrasenia1, listaTargets) 
            #seguidor(usuario2, contrasenia2, listaTargets)  
            seguidor(usuario3, contrasenia3, listaTargets)                                      
            time.sleep(tiempoLoops + 10*random.random()) 
    except: 
        time.sleep(tiempoLoops + 10*random.random())      



        
