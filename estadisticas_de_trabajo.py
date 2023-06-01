import datetime
import os

fecha_actual = datetime.date.today()
fecha_anterior = fecha_actual - datetime.timedelta(days=7)

contador_ficheros = {}

for root, dirs, files in os.walk("."):
    for file in files:
        ruta_fichero = os.path.join(root, file)
        fecha_modificacion = datetime.date.fromtimestamp(os.path.getmtime(ruta_fichero))

        if fecha_anterior <= fecha_modificacion <= fecha_actual:
            contador_ficheros[fecha_modificacion] = (
                contador_ficheros.get(fecha_modificacion, 0) + 1
            )

# Mostrar el gráfico de barras en la terminal
for fecha, cantidad in sorted(contador_ficheros.items()):
    barra = "\u2589" * cantidad
    print(f"{fecha} {barra}")
