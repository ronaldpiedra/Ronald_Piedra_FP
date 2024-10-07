# Escritura de Archivo de Texto

# Abre (o crea) el archivo my_notes.txt en modo escritura
with open('my_notes.txt', 'w') as file:
    # Escribe notas personales en el archivo
    file.write("Nota 1: Recuerda estudiar para el examen.\n")
    file.write("Nota 2: Comprar víveres este fin de semana.\n")
    file.write("Nota 3: Llamar a mamá el viernes.\n")

# Lectura de Archivo de Texto

# Abre el archivo my_notes.txt en modo lectura
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra en la consola cada línea leída
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final

