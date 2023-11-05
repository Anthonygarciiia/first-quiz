import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instrucciones:
# Pregunta 4 y Pregunta 5 tratan de escribir SQL.Usan la base de datos que es
# Creado en el archivo `Pets_db.py`.
# Estas preguntas utilizan una base de datos llamada SQLite.No necesita instalar nada.
# En el archivo se crean tres tablas.Luego se agregan datos a cada uno
# de las tablas.Las preguntas a continuación son sobre cómo los datos en cada una de las tablas
# está relacionado.

# Parte 4.A:
# Escribe SQL para seleccionar las mascotas que son propiedad de nadie.
# La salida debe ser una lista de tuplas en el formato: (<nombre de mascota>, <pecies>, <ge>)

sql_pets_owned_by_nobody = """
SELECT a.name, a.species, a.age
FROM animals a
LEFT JOIN people_animals pa ON a.animal_id = pa.pet_id
WHERE pa.owner_id IS NULL;
"""

# Part 4.B:
# Escriba SQL para seleccionar cómo el número de mascotas es más antigua que sus dueños.
# La salida debe ser un entero.

sql_pets_older_than_owner = """
SELECT COUNT(*) AS num_pets_older_than_owners
FROM people_animals pa
JOIN animals a ON pa.pet_id = a.animal_id
JOIN people p ON pa.owner_id = p.person_id
WHERE a.age > p.age;
"""

# Part 4.C: ¡Desafío de bonificación!
# Escribe SQL para seleccionar las mascotas que son propiedad de Bessie y nadie más.
# La salida debe ser una lista de tuplas en el formato: (<nombre de la persona>, <nombre de mascota>, <pecies>)
sql_only_owned_by_bessie = """ 
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM people p
JOIN people_animals pa ON p.person_id = pa.owner_id
JOIN animals a ON pa.pet_id = a.animal_id
WHERE p.name = 'bessie'
  AND NOT EXISTS (
    SELECT 1
    FROM people_animals pa_other
    WHERE pa_other.pet_id = pa.pet_id
      AND pa_other.owner_id != p.person_id
  );
"""