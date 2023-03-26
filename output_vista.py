import time

# Nombre del archivo a leer
filename = "output.txt"

# Abrir el archivo en modo lectura
with open("output.txt", "r") as f:
    # Bucle infinito para leer continuamente el archivo
    while True:
        # Leer el contenido del archivo
        content = f.read()
        # Si hay contenido, mostrarlo en la consola
        if content:
            print(content)
        # Esperar 1 segundo antes de volver a leer el archivo
        time.sleep(1)