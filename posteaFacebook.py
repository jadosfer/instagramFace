import logging
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

#---------------------- seteos
usuario = "jadosfer@hotmail.com"
clave = "Yooooo"

#100272043448819 requiere iniciar conversacion

groups = [275366519230814, 153631318156973, 287034871493135, 1199440190106196, 652626034853411,1665015093823153,
1426675940934614, 182925021771043, 161293957920722, 302971293635942, 912523932450311, 581681948572216,
581681948572216, 1399974050239330, 988580631186225, 334590160467895, 411811655989675, 1410559132569743, 
265749977090837, 617981228580882, 265475913933345, 802924396565923, 1971185586238081, 247175739392548, 
771022723278866, 1446812668915456, 1507453949547213, 323679908191117, 118954581940030, 782207818466243, 
1682737798681872, 2265885220354929, 188007908541197, 365818130458364, 733342683362694, 119217145422978, 
1443539405954202, 820355148340300, 271645632991456, 685405254999981, 1051533001572433, 1370942556284938, 1612144055689619, 
335970929803798, 1212309382270403]

pyautogui.keyDown('win')
pyautogui.keyDown('d')
pyautogui.keyUp('d')
pyautogui.keyUp('win')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('e')
pyautogui.keyUp('e')
pyautogui.keyUp('ctrl')

pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('up')
pyautogui.press('enter')

time.sleep(1)
pyautogui.write('https://facebook.com/')
pyautogui.press('enter')
time.sleep(3)
pyautogui.write(usuario)
pyautogui.press('tab')
pyautogui.write(clave)
pyautogui.press('enter')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('l')
pyautogui.keyUp('l')
pyautogui.keyUp('ctrl')

for group in groups:
    pyautogui.write('https://facebook.com/groups/{}'.format(group))
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.press('p')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite("""Hola a todos! Les comparto un nuevo video de mi Curso de Programacion en Python donde comenzamos a aprender a usar Git y Github. Saludos!

https://youtu.be/MuK5NbABwa4

el curso completo aqui:

https://www.youtube.com/watch?v=2IRqwNFV_ho&list=PLRdPbj58cT84-cJ3TTJi8PThFIL8wTC_a""")
    
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    time.sleep(4)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')
    pyautogui.keyUp('ctrl')

pyautogui.keyDown('alt')
pyautogui.keyDown('f4')
pyautogui.keyUp('f4')
pyautogui.keyUp('alt')
