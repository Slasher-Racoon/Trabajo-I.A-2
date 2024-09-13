import random
import math

# Función que genera un número aleatorio entre 1 y 6, simulando un dado de 6 caras
def lanzar_dado():
    return random.randint(1, 6)

# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Función que maneja el turno de un jugador, incluyendo la opción de lanzar dados adicionales
def turno_jugador(jugador):
    dado1 = lanzar_dado()
    dado2 = lanzar_dado()
    suma = dado1 + dado2

    print(f"Turno del jugador {jugador}:")
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")

    # Verificamos si el jugador sacó dobles
    if dado1 == dado2:
        opcion_dividir = input("¡Sacaste dobles! ¿Deseas dividir tu lanzamiento y lanzar 3 dados adicionales por cada parte? (s/n): ").lower()

        if opcion_dividir == 's':
            suma_div1 = dado1  # Primer grupo
            suma_div2 = dado2  # Segundo grupo

            # Lanzamos 3 dados adicionales para cada división
            print("Lanzando 3 dados adicionales para la primera división:")
            for i in range(3):
                dado = lanzar_dado()
                suma_div1 += dado
                print(f"Dado {i + 1}: {dado}")

            print(f"Suma de la primera división: {suma_div1}")

            print("Lanzando 3 dados adicionales para la segunda división:")
            for i in range(3):
                dado = lanzar_dado()
                suma_div2 += dado
                print(f"Dado {i + 1}: {dado}")

            print(f"Suma de la segunda división: {suma_div2}")

            # Elegimos la suma mayor de las dos divisiones como la suma final
            suma = max(suma_div1, suma_div2)
            print(f"Se elige la mayor suma entre las dos divisiones: {suma}")
        else:
            print("Decidiste no dividir tu lanzamiento.")
    
    print(f"Suma inicial (sin división o tras división): {suma}")

    while suma <= 23:
        opcion = input(f"Jugador {jugador}, ¿quieres lanzar un dado adicional? (s/n): ").lower()

        if opcion == 'n':
            break  # Si el jugador no quiere lanzar otro dado, termina el turno

        dado_adicional = lanzar_dado()
        suma += dado_adicional

        print(f"Dado adicional: {dado_adicional}")
        print(f"Nueva suma total: {suma}")

        if suma > 23:
            print(f"¡La suma total supera 23! Fin del turno para el jugador {jugador}.")
            break

    print(f"Suma final del jugador {jugador}: {suma}\n")
    return suma

# Función para determinar el ganador basado en las reglas especificadas
def determinar_ganador(suma_a, suma_b):
    # Verificamos si algún jugador tiene exactamente 23
    if suma_a == 23 and suma_b != 23:
        print("El Jugador A gana con exactamente 23 puntos.")
        return
    elif suma_b == 23 and suma_a != 23:
        print("El Jugador B gana con exactamente 23 puntos.")
        return
    elif suma_a == 23 and suma_b == 23:
        print("Ambos jugadores tienen exactamente 23 puntos. ¡Empate!")
        return

    # Verificamos si ambos jugadores se pasaron de 23
    if suma_a > 23 and suma_b > 23:
        print("Ambos jugadores se pasaron de 23. ¡No hay ganador!")
        return
    elif suma_a > 23:
        print("El Jugador A se pasó de 23. El Jugador B gana.")
        return
    elif suma_b > 23:
        print("El Jugador B se pasó de 23. El Jugador A gana.")
        return

    # Verificamos los números primos
    primo_a = es_primo(suma_a)
    primo_b = es_primo(suma_b)

    if primo_a and not primo_b:
        print("El Jugador A gana con un número primo.")
        return
    elif primo_b and not primo_a:
        print("El Jugador B gana con un número primo.")
        return
    elif primo_a and primo_b:
        if suma_a > suma_b:
            print("Ambos jugadores tienen números primos. El Jugador A gana con un número primo más alto.")
        elif suma_b > suma_a:
            print("Ambos jugadores tienen números primos. El Jugador B gana con un número primo más alto.")
        else:
            print("Ambos jugadores tienen el mismo número primo. ¡Empate!")
        return

    # Si ninguno tiene número primo, gana el que esté más cerca de 23
    if abs(23 - suma_a) < abs(23 - suma_b):
        print("El Jugador A gana por estar más cerca de 23.")
    elif abs(23 - suma_b) < abs(23 - suma_a):
        print("El Jugador B gana por estar más cerca de 23.")
    else:
        print("Ambos jugadores están a la misma distancia de 23. ¡Empate!")

# Función principal
def main():
    # Turno del Jugador A
    suma_a = turno_jugador("A")

    # Turno del Jugador B
    suma_b = turno_jugador("B")

    print("Resultados finales:")
    print(f"Suma final del Jugador A: {suma_a}")
    print(f"Suma final del Jugador B: {suma_b}\n")

    # Determinar el ganador
    determinar_ganador(suma_a, suma_b)

if __name__ == "__main__":
    main()
