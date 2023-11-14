""" /*
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 */
 """

import random

print("""
👻 BoooOOOooOoo!
Si quieres encontrar los dulces 🍭 de la casa encantada 🏰
tendrás que buscarlos a través de sus habitaciones.
Pero recuerda, no podrás moverte si antes no respondes 
correctamente a su enigma.      
""")


def crear_casa() -> (list, list):
    casa = [["⬜️"] * 4 for _ in range(4)]

    if random.choice([True, False]):
        # Columnas perimetro
        puerta = [random.randint(0, 3), random.choice([0, 3])]
    else:
        # Filas perimetro
        puerta = [random.choice([0, 3]), random.randint(0, 3)]

    casa[puerta[0]][puerta[1]] = "🚪"

    def colocar_caramelo(puerta: list) -> list:
        # Colocando caramelo
        caramelo = [random.randint(0, 3), random.randint(0, 3)]

        if caramelo[0] == puerta[0] and caramelo[1] == [1]:
            return colocar_caramelo(puerta)

        return caramelo

    caramelo = colocar_caramelo(puerta)

    casa[caramelo[0]][caramelo[1]] = "🍭"

    for row in casa:
        print("".join(map(str, row)))

    return casa, puerta


def muevete(posicion: list) -> list:

    row, col = posicion[0], posicion[1]

    movimientos = "N S E O "

    if row == 0:
        movimientos = movimientos.replace("N", "")
    if row == 3:
        movimientos = movimientos.replace("S", "")
    if col == 0:
        movimientos = movimientos.replace("O", "")
    if col == 3:
        movimientos = movimientos.replace("E", "")

    movimiento = input(
        f"¿Hacia donde te quieres mover [ {movimientos} ]?: ").upper()

    if movimiento in movimientos:
        if movimiento == "N":
            posicion = [row - 1, col]
        elif movimiento == "S":
            posicion = [row + 1, col]
        elif movimiento == "E":
            posicion = [row, col + 1]
        elif movimiento == "O":
            posicion = [row, col - 1]

        return posicion

    else:
        print("Desplazamiento incorrecto. Seleccione una de las opciones válidas.")
        return muevete(posicion)


casa, puerta = crear_casa()

posicion = puerta

print(f"Posicion inicial: {posicion}")


def acertijo():

    acertijos = [("¿Lenguaje para apps Android?", "Kotlin"),
                 ("¿Lenguaje web para estilos?", "CSS"),
                 ("¿Traduce código antes de ejecutar?", "Compilador"),
                 ("¿Almacena datos y código?", "Objeto"),
                 ("¿Repite código mientras se cumple condición?", "Bucle"),
                 ("¿Conjunto de reglas para tareas específicas?", "Algoritmo"),
                 ("¿Traduce línea por línea durante ejecución?", "Interprete"),
                 ("¿Espacio de almacenamiento con nombre?", "Variable"),
                 ("¿Almacena elementos en secuencia?", "Array"),
                 ("¿Paradigma con objetos y métodos?", "POO"),
                 ("¿Proceso de corregir errores?", "Debugging"),
                 ("¿Bloque de código independiente?", "Funcion"),
                 ("¿Sistema de control de versiones?", "Git"),
                 ("¿Estructura de control con número de repeticiones?", "Bucle for"),
                 ("¿Interfaz para comunicación entre aplicaciones?", "API"),
                 ("¿Función que se llama a sí misma?", "Recursividad"),
                 ("¿Creación de versiones virtuales?", "Virtualizacion"),
                 ("¿Enfoque de desarrollo colaborativo y flexible?", "Desarrollo agil"),
                 ("¿Paradigma que evita cambio de estado?", "Funcional"),
                 ("¿Programa que responde a solicitudes web?", "Servidor web")]

    acertijo_aleatorio = acertijos[random.randint(0, len(acertijos)-1)]

    while True:
        respuesta = input(f"{acertijo_aleatorio[0]}: ")

        if respuesta.lower() == acertijo_aleatorio[1].lower():
            print("Respuesta correcta!\n")
            return
        else:
            print("Respuesta incorrecta!\n")


muevete(posicion)

while True:

    posicion = muevete(posicion)
    print(f"Posicion: {posicion}")

    habitacion_casa = casa[posicion[0]][posicion[1]]

    if habitacion_casa == "⬜️":

        print("Responde correctamente a esta pregunta")
        acertijo()

        fantasma = random.randint(1, 10) == 1
        if fantasma:
            print(
                "👻 BoooOOooO! Para salir de esta habitación deberás responder otra pregunta más.")
            acertijo()

    elif habitacion_casa == "🍭":
        print("""
    👻 BoooOOooO!
    Has encontrado los dulces 🍭 y escapado de la casa encantada 🏰
    ¡ Feliz Halloween ! 🎃
    """)
        break
