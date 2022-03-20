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
        tiempo = 60  #segundos


#---------------------> Hace la plantacion <---------------------#
        def presionarSpace():
                pyautogui.press('space')
                print('Plantacion completado')
                tiempo = 14400  #segundos
                t = Timer(tiempo, presionar2)
                t.start()

#---------------------> hace el riego despues de 4hs pasada la plantacion <---------------------#
        def presionar2():
                pyautogui.press('space')
                print('riego 1 completado')
                t = Timer(tiempo, presionar3)
                t.start()

#---------------------> hace el riego despues de 8hs pasada la plantacion <---------------------#
        def presionar3():
                pyautogui.press('space')
                print('riego 2 completado')
                t = Timer(tiempo, presionar4)
                t.start()

#---------------------> hace el riego despues de 12hs pasada la plantacion <---------------------#
        def presionar4():
                pyautogui.press('space')
                print('riego 3 completado')
                t = Timer(tiempo, presionar5)
                t.start()

#---------------------> hace el riego despues de 16hs pasada la plantacion <---------------------#
        def presionar5():
                pyautogui.press('space')
                print('riego 4 completado')
                exit()


#---------------------> tenemos que cosechar pasadas las 8hs <---------------------#


        t = Timer(tiempo, presionarSpace)
        t.start()
