# Un diccionario en Python nos permite almacenar información en pares clave-valor.
# En este caso, creamos un diccionario que contiene datos ficticios sobre una persona.
informacion_personal = {
    "nombre": "Juan Jose",  # Clave 'nombre', con el valor 'Carlos Pérez'
    "edad": 18,                # Clave 'edad', con el valor 29
    "ciudad": "Quito",         # Clave 'ciudad', con el valor 'Quito'
    "profesion": "Ingeniero de Software"  # Clave 'profesion', con el valor 'Ingeniero de Software'
}

# Imprimimos el diccionario original para ver cómo está desde el principio.
print("Diccionario original:", informacion_personal)

# Ahora, vamos a cambiar el valor de la clave 'ciudad'. Antes estaba Quito, pero ahora será Guayaquil.
# Accedemos a la clave 'ciudad' y le asignamos un nuevo valor.
informacion_personal["ciudad"] = "Guayaquil"


# Aunque ya existe una clave 'profesion', podemos asignarle un nuevo valor si queremos actualizarla.
# En este caso, la cambiamos a "Desarrollador Web".
informacion_personal["profesion"] = "Abogado"

# Verificar si existe la clave 'telefono'
# Antes de agregar un teléfono, tenemos que verificar si ya existe esa clave en el diccionario.
# Usamos la palabra clave 'if' para preguntar si 'telefono' no está en el diccionario.
if "telefono" not in informacion_personal:
    # Si la clave 'telefono' no existe, la agregamos con un número ficticio.
    informacion_personal["telefono"] = "0987654321"

# Eliminar una clave
# En este paso, eliminamos la clave 'edad'.
# Usamos el metodo pop para eliminarla. El segundo argumento (None) previene un error si la clave no existiera.
informacion_personal.pop("edad", None)

# Imprimimos el diccionario final para ver todos los cambios que hemos hecho.
print("Diccionario final:", informacion_personal)
