# imports
from time import time_ns, timezone
import pyautogui
import sys
from pymsgbox import *
from threading import Timer
import vaca as v
import lechuga as l
import manzana as m
import pez as p
import prueba as pr


# SELECIONAR CULTIVO
OPT_VACA = "VACA"
OPT_LECHUGA = "LECHUGA"
OPT_MANZANA = "MANZANA"
OPT_PEZ = "PEZ"
OPT_CERRAR = "CERRAR"
OPT_PRUEBA = "PRUEBA"

# Botones.
OPT_INICIAR = "Iniciar Plantacion"
OPT_VOLVER = "Volve"
OPT_SI = "SI"
OPT_NO = "NO"
# ------------- MENU INICIAL ------------------ #
def menuInicial():

    opt = pyautogui.confirm(
        "¿Que cultivo vas a regar?",
        "Seleccionar uno",
        [OPT_VACA, OPT_LECHUGA, OPT_MANZANA, OPT_PEZ, OPT_PRUEBA, OPT_CERRAR]
    )
    if opt == OPT_VACA:
        v.riego()

    elif opt == OPT_LECHUGA:
        l.riego()
    elif opt == OPT_MANZANA:
        m.riego()
    elif opt == OPT_PEZ:
        p.riego()
    elif opt == OPT_PRUEBA:
        pr.riego()
    
    elif opt == OPT_CERRAR:
     opt = pyautogui.confirm(
        "Seguro que queres cerrar?:",
        "Confirmación",
        [OPT_SI, OPT_NO]
     )
     if opt == OPT_NO:
        menuInicial()

     elif opt == OPT_SI:
        exit()



menuInicial()





#               .-""""-.
#              /        \
#             /_        _\
#            // \      / \\
#            |\__\    /__/|
#             \    ||    /
#              \        /
#               \  __  /  \  /          ________________________________
#                '.__.'    \/          /                                 \
#                 |  |     /\         |     te acabas de encontrar       |
#                 |  |    O  O        |    con el alien Robertito!       |
#                 ----    //         O \_________________________________/
#                (    )  //        O
#               (\\     //       o
#              (  \\    )      o
#              (   \\   )   /\
#    ___[\______/^^^^^^^\__/) o-)__
#   |\__[=======______//________)__\
#   \|_______________//____________|
#       |||      || //||     |||
#       |||      || @.||     |||
#        ||      \/  .\/      ||
#                   . .
#                  '.'.`
