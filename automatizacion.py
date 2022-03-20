# imports
import pyautogui
import sys
from pymsgbox import *
from threading import Timer

# Botones.
OPT_INICIAR = "Iniciar Plantacion"
OPT_CERRAR = "Cerrar"

# Crear el mensaje
opt = pyautogui.confirm(
    "¿Que queres hacer paa?",
    "Confirmación",
    [OPT_INICIAR, OPT_CERRAR]
)

# Tomar decisión en base al botón presionado.
if opt == OPT_CERRAR:
    exit()
elif opt == OPT_INICIAR:

    i = 0;
    tiempo = 5  #segundos

    def presionarSpace():
            pyautogui.press('space')
            print('riego 1 completado')
            t = Timer(tiempo, presionar2)
            t.start()

    def presionar2():
            pyautogui.press('space')
            print('riego 2 completado')
            exit()
  
    t = Timer(tiempo, presionarSpace)
    t.start()



