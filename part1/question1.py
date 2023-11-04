################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instrucciones:
# Las dos funciones a continuación se utilizan para decir el clima.Tienen algunos errores que
# Necesita ser reparado.El conjunto de pruebas en `Question1_test.py` verificará la salida.
# Lea el conjunto de pruebas para conocer los valores que estas funciones deberían devolver.

def get_city_temperature(city):
   if city == "Quito":
      return 22
   if city == "Sao Paulo":
      return 17
   if city == "San Francisco":
      return 16
   if city == "New York":
      return 14

def get_city_weather(city):

  sky_condition = None

  if city == "Sao Paulo":
     sky_condition = "cloudy"
  elif city == "New York":
     sky_condition = "rainy"
  elif city == "Quito":
     sky_condition = "sunny"
  temperature = get_city_temperature(city)

  return str(temperature) + " degrees and " + sky_condition
