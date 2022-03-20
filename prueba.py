# imports
import pyautogui
import sys
# import main as script
from pymsgbox import *
from threading import Timer





def riego():

    #------------------Botones------------------#
    OPT_INICIAR = "Iniciar Plantacion"
    OPT_VOLVER = "volver"

    #------------------Menu de Confirmacion------------------#

    opt = pyautogui.confirm(
    "¿Que queres hacer?",
    "Confirmación",
    [OPT_INICIAR, OPT_VOLVER]
    )

    #------------------Si toca volver------------------#

    if opt == OPT_VOLVER:
        # script.menuInicial()
        print('hola')
    #------------------Si inicia------------------#

    
    elif opt == OPT_INICIAR:

        i = 0;
        tiempo = 10  #segundos


#---------------------> Hace la plantacion <---------------------#
        def presionarSpace():
                pyautogui.press('x')
                print('Plantacion completado')
                tiempo = 5  #segundos
                t = Timer(tiempo, presionar2)
                t.start()

#---------------------> hace el riego despues de 4hs pasada la plantacion <---------------------#
        def presionar2():
                pyautogui.press('x')
                print('riego 1 completado')
                tiempo = 5  #segundos
                t = Timer(tiempo, presionar3)
                t.start()

#---------------------> hace el riego despues de 8hs pasada la plantacion <---------------------#
        def presionar3():
                pyautogui.press('x')
                print('riego 2 completado')
                exit()



#---------------------> tenemos que cosechar pasadas las 2hs <---------------------#


        t = Timer(tiempo, presionarSpace)
        t.start()
