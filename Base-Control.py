import random
import math

# Función para lanzar un dado
def lanzar_dado():
    return random.randint(1, 6)  # Generar un número aleatorio entre 1 y 6

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Función para manejar el turno de cada jugador, incluyendo las reglas especiales de dobles y 12
def turno_jugador(jugador):
    dado1 = lanzar_dado()
    dado2 = lanzar_dado()
    suma_total = dado1 + dado2

    # Mostrar los resultados iniciales
    print(f"Jugador {jugador} - Dado 1: {dado1}")
    print(f"Jugador {jugador} - Dado 2: {dado2}")
    print(f"Jugador {jugador} - Suma inicial de los dados: {suma_total}")

    # Caso especial: si el jugador saca dobles
    if dado1 == dado2:
        respuesta = input(f"Jugador {jugador}, has sacado dobles ({dado1}). ¿Deseas dividir tu lanzamiento y lanzar 3 dados adicionales para cada división? (s/n): ").lower()
        if respuesta == 's':
            suma_division1 = dado1
            suma_division2 = dado2

            print(f"Lanzando 3 dados para la primera división (inicial con {dado1}):")
            for i in range(3):
                dado_adicional = lanzar_dado()
                suma_division1 += dado_adicional
                print(f"Dado adicional {i + 1}: {dado_adicional}")
            print(f"Suma total de la primera división: {suma_division1}")

            print(f"Lanzando 3 dados para la segunda división (inicial con {dado2}):")
            for i in range(3):
                dado_adicional = lanzar_dado()
                suma_division2 += dado_adicional
                print(f"Dado adicional {i + 1}: {dado_adicional}")
            print(f"Suma total de la segunda división: {suma_division2}")

            # Elegir la suma mayor de las dos divisiones
            suma_total = max(suma_division1, suma_division2)
            print(f"Jugador {jugador}, se ha elegido la mayor suma: {suma_total}")

    # Caso especial: si el jugador saca 12
    if suma_total == 12:
        respuesta = input(f"Jugador {jugador}, has sacado un 12. ¿Deseas lanzar solo 1 dado adicional para alcanzar un máximo de 18? (s/n): ").lower()
        if respuesta == 's':
            dado_adicional = lanzar_dado()
            suma_total += dado_adicional
            print(f"Jugador {jugador} - Dado adicional: {dado_adicional}")
            print(f"Nueva suma total: {suma_total}")
            return suma_total

    # Preguntar si desea lanzar más dados si no se han pasado de 23
    while suma_total <= 23:
        respuesta = input(f"Jugador {jugador}, ¿deseas lanzar un dado adicional? (s/n): ").lower()
        if respuesta == 'n':
            break  # El jugador decide no lanzar más dados

        # Si el jugador elige lanzar un dado adicional
        dado_adicional = lanzar_dado()
        suma_total += dado_adicional

        print(f"Jugador {jugador} - Dado adicional: {dado_adicional}")
        print(f"Jugador {jugador} - Nueva suma total: {suma_total}")

        # Verificar si la suma supera 23
        if suma_total > 23:
            print(f"Jugador {jugador}, te has pasado de 23 con una suma total de {suma_total}")
            break

    return suma_total

# Función para determinar el ganador con las condiciones especificadas
def determinar_ganador(suma_a, suma_b):
    # 0. Verificar si alguno de los jugadores tiene exactamente 23
    if suma_a == 23 and suma_b == 23:
        print("¡Ambos jugadores tienen 23! ¡Es un empate perfecto!")
        return
    elif suma_a == 23:
        print("¡Jugador A gana con exactamente 23 puntos!")
        return
    elif suma_b == 23:
        print("¡Jugador B gana con exactamente 23 puntos!")
        return

    # 1. Prioridad para números primos
    primo_a = es_primo(suma_a)
    primo_b = es_primo(suma_b)

    if primo_a and not primo_b:
        print(f"¡Jugador A gana con un número primo ({suma_a})!")
        return
    elif not primo_a and primo_b:
        print(f"¡Jugador B gana con un número primo ({suma_b})!")
        return

    # 3. Verificar quién está más cerca de 23 sin pasarse
    if suma_a <= 23 and suma_b > 23:
        print("Jugador B se pasó de 23. ¡Jugador A gana!")
        return
    elif suma_b <= 23 and suma_a > 23:
        print("Jugador A se pasó de 23. ¡Jugador B gana!")
        return
    elif suma_a <= 23 and suma_b <= 23:
        distancia_a = 23 - suma_a
        distancia_b = 23 - suma_b

        if distancia_a < distancia_b:
            print("¡Jugador A gana por estar más cerca de 23!")
        elif distancia_b < distancia_a:
            print("¡Jugador B gana por estar más cerca de 23!")
        else:
            print("¡Es un empate! Ambos jugadores están igual de cerca de 23.")
    else:
        print("Ambos jugadores se pasaron de 23. ¡No hay ganador!")

# Main
def main():
    random.seed()

    # Turno del Jugador A
    print("Turno del Jugador A")
    suma_a = turno_jugador('A')
    print()

    # Turno del Jugador B
    print("Turno del Jugador B")
    suma_b = turno_jugador('B')
    print()

    # Mostrar la suma total de ambos jugadores
    print(f"Suma total de los lanzamientos del Jugador A: {suma_a}")
    print(f"Suma total de los lanzamientos del Jugador B: {suma_b}")

    # Determinar el ganador basado en las condiciones
    determinar_ganador(suma_a, suma_b)

if __name__ == "__main__":
    main()
