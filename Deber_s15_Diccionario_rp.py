# Crear un diccionario llamado 'informacion_personal' con información ficticia.
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave 'ciudad' y modificarlo.
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos la ciudad a Guayaquil.

# Agregar una nueva clave-valor para representar la 'profesion' de la persona.
informacion_personal["profesion"] = "Desarrollador de Software"  # Actualizamos la profesión.

# Verificar si la clave 'telefono' existe en el diccionario.
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio.
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave 'edad' del diccionario.
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la clave 'edad'.

# Imprimir el diccionario resultante después de realizar todas las operaciones.
print(informacion_personal)
