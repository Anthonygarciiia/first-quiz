################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instrucciones:
# Escriba una función que intercambie una tupla de dos elementos.Por ejemplo, la función
# debería cambiar (x, y) en (y, x).
# Asigna la función a `swapper` para que la función` run_swapper (..) `pueda usar
# él.Como siempre, hay un conjunto de pruebas que verifica el resultado.Está dentro
# `pregunta2_test.py.`

def swapperfun(tupla):
    if len(tupla) == 2:
        x, y = tupla
        return (y, x)
    else:
        return None

swapper = swapperfun

def run_swapper(list_of_tuples):
  return list(map(swapper, list_of_tuples))