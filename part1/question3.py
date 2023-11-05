################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instrucciones:
# Haz una clase de Python para un horno mágico que pueda combinar ingredientes en
# diferentes temperaturas para elaborar materiales especiales.
#
# La clase de horno debe tener los métodos:
# - Agregar (elemento) para agregar un horno para combinar
# - congelarse () para congelar los ingredientes
# - hervir () para hervir los ingredientes
# - espera () para combinar los ingredientes sin cambios en la temperatura
# - get_output () para obtener el resultado
#
# Deberá cambiar la función `make_oven ()` para devolver una nueva instancia
# de tu horno.
#
# La función `alchemy_combine ()` usará su horno.Puedes ver la esperada
# Fórmulas y sus salidas en el archivo de prueba, `pregunta3_test.py`.

# ¡Esta función debería devolver una instancia de horno!

class MagicalOven:
    def __init__(self):
        self.ingredients = []
        self.output = None

    def add(self, element):
        self.ingredients.append(element)

    def freeze(self):
        for ingredient in self.ingredients:
            if ingredient == "cheese" or ingredient == "dough" or ingredient == "tomato":
                # Cambiar ingredientes a "frozen ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "frozen " + ingredient
                self.output = "pizza"  # Establecer la salida en "pizza"
        if ingredient == "water" or ingredient == "air":
                # Cambiar ingredientes a "frozen ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "frozen " + ingredient
                self.output = "snow"  # Establecer la salida en "snow"
        if ingredient == "lead" or ingredient == "mercury":
                # Cambiar ingredientes a "frozen ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "frozen " + ingredient
                self.output = "gold"  # Establecer la salida en "gold"
    def boil(self):
        for ingredient in self.ingredients:
            if ingredient == "cheese" or ingredient == "dough" or ingredient == "tomato":
                # Cambiar ingredientes a "boiled ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "boiled " + ingredient
                self.output = "pizza"  # Establecer la salida en "pizza"
            if ingredient == "water" or ingredient == "air":
                # Cambiar ingredientes a "boiled ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "boiled " + ingredient
                self.output = "snow"  # Establecer la salida en "snow"
            if ingredient == "lead" or ingredient == "mercury":
                # Cambiar ingredientes a "frozen ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "frozen " + ingredient
                self.output = "gold"  # Establecer la salida en "gold"

    def wait(self):
        for ingredient in self.ingredients:
            if ingredient == "cheese" or ingredient == "dough" or ingredient == "tomato":
                # Cambiar ingredientes a "mixed ingredients"
                self.ingredients[self.ingredients.index(ingredient)] = "mixed ingredients"
                self.output = "pizza"  # Establecer la salida en "pizza"
            if ingredient == "water" or ingredient == "air":
                # Cambiar ingredientes a "boiled ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "boiled " + ingredient
                self.output = "snow"  # Establecer la salida en "snow"
            if ingredient == "lead" or ingredient == "mercury":
                # Cambiar ingredientes a "frozen ingredient"
                self.ingredients[self.ingredients.index(ingredient)] = "frozen " + ingredient
                self.output = "gold"  # Establecer la salida en "gold"
       

    def get_output(self):
        return self.output

def make_oven():
    return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
