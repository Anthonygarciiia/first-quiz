################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instrucciones:
# Estas preguntas continúan utilizando la base de datos con la que trabajamos en la pregunta 4. En
# Esta pregunta, haremos algunas modificaciones de la tabla.

# Parte 5.A:
# Crea una nueva tabla,'favorite_foods.' Debe tener las columnas:
# food_id integer
# name text
# vegetarian integer

sql_create_favorite_foods = """
CREATE TABLE favorite_foods (
          food_id integer,
          name text not null,
          vegetarian integer
        );
"""

# Part 5.B:
# Altere las tablas de animales y personas agregando una nueva columna a cada una llamada 'favoritas_food_id'
# El conjunto de pruebas verificará los nuevos cambios insertando algunas filas nuevas.

sql_alter_tables_with_favorite_food = """
ALTER TABLE animals
        ADD COLUMN favorite_food_id integer;
ALTER TABLE people
        ADD COLUMN favorite_food_id integer;
"""

# Part 5.C:
# Escriba una consulta para seleccionar todas las mascotas que sean vegetarianas.
# La salida debe ser una lista de tuplas en el formato: (<nombre de mascota>, <Nombre de la comida>)

sql_select_all_vegetarian_pets = """
SELECT a.name AS pet_name, ff.name AS food_name
        FROM animals a
        JOIN favorite_foods ff ON a.favorite_food_id = ff.food_id
        WHERE ff.vegetarian = 1;
"""