archivo = open('my_notes.txt', 'w')

# Escribo tres líneas de notas en el archivo
archivo.write("Linea 1: Semana16\n")
archivo.write("Linea 2: Adrian Villegas Semana16\n")
archivo.write("Linea 3: Semana16\n")

archivo.close()

archivo = open('my_notes.txt', 'r')

linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()

archivo.close()
