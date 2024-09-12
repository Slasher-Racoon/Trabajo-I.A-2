#include <iostream>
#include <cstdlib> // para rand() y srand()
#include <ctime>   // para time()
#include <cmath>   // para abs()

// Función para lanzar un dado
int lanzarDado() {
    return (rand() % 6) + 1; // Generar un número aleatorio entre 1 y 6
}

// Función para verificar si un número es primo
bool esPrimo(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

// Función para manejar el turno de cada jugador, incluyendo las reglas especiales de dobles y 12
void turnoJugador(char jugador, int& suma_total) {
    int dado1 = lanzarDado();
    int dado2 = lanzarDado();
    suma_total = dado1 + dado2;

    // Mostrar los resultados iniciales
    std::cout << "Jugador " << jugador << " - Dado 1: " << dado1 << std::endl;
    std::cout << "Jugador " << jugador << " - Dado 2: " << dado2 << std::endl;
    std::cout << "Jugador " << jugador << " - Suma inicial de los dados: " << suma_total << std::endl;

    // Caso especial: si el jugador saca dobles
    if (dado1 == dado2) {
        char respuesta;
        std::cout << "Jugador " << jugador << ", has sacado dobles (" << dado1 << "). ¿Deseas dividir tu lanzamiento y lanzar 3 dados adicionales para cada división? (s/n): ";
        std::cin >> respuesta;

        if (respuesta == 's' || respuesta == 'S') {
            int suma_division1 = dado1, suma_division2 = dado2;

            std::cout << "Lanzando 3 dados para la primera división (inicial con " << dado1 << "):\n";
            for (int i = 0; i < 3; i++) {
                int dado_adicional = lanzarDado();
                suma_division1 += dado_adicional;
                std::cout << "Dado adicional " << (i + 1) << ": " << dado_adicional << std::endl;
            }
            std::cout << "Suma total de la primera división: " << suma_division1 << std::endl;

            std::cout << "Lanzando 3 dados para la segunda división (inicial con " << dado2 << "):\n";
            for (int i = 0; i < 3; i++) {
                int dado_adicional = lanzarDado();
                suma_division2 += dado_adicional;
                std::cout << "Dado adicional " << (i + 1) << ": " << dado_adicional << std::endl;
            }
            std::cout << "Suma total de la segunda división: " << suma_division2 << std::endl;

            // Elegir la suma mayor de las dos divisiones
            suma_total = std::max(suma_division1, suma_division2);
            std::cout << "Jugador " << jugador << ", se ha elegido la mayor suma: " << suma_total << std::endl;
        }
    }

    // Caso especial: si el jugador saca 12
    if (suma_total == 12) {
        char respuesta;
        std::cout << "Jugador " << jugador << ", has sacado un 12. ¿Deseas lanzar solo 1 dado adicional para alcanzar un máximo de 18? (s/n): ";
        std::cin >> respuesta;

        if (respuesta == 's' || respuesta == 'S') {
            int dado_adicional = lanzarDado();
            suma_total += dado_adicional;
            std::cout << "Jugador " << jugador << " - Dado adicional: " << dado_adicional << std::endl;
            std::cout << "Nueva suma total: " << suma_total << std::endl;
            return;
        }
    }

    // Preguntar si desea lanzar más dados si no se han pasado de 23
    char respuesta;
    while (suma_total <= 23) {
        std::cout << "Jugador " << jugador << ", ¿deseas lanzar un dado adicional? (s/n): ";
        std::cin >> respuesta;

        if (respuesta == 'n' || respuesta == 'N') {
            break; // El jugador decide no lanzar más dados
        }

        // Si el jugador elige lanzar un dado adicional
        int dado_adicional = lanzarDado();
        suma_total += dado_adicional;

        std::cout << "Jugador " << jugador << " - Dado adicional: " << dado_adicional << std::endl;
        std::cout << "Jugador " << jugador << " - Nueva suma total: " << suma_total << std::endl;

        // Verificar si la suma supera 23
        if (suma_total > 23) {
            std::cout << "Jugador " << jugador << ", te has pasado de 23 con una suma total de " << suma_total << std::endl;
            break;
        }
    }
}

// Función para determinar el ganador con las condiciones especificadas
void determinarGanador(int suma_a, int suma_b) {
    // 0. Verificar si alguno de los jugadores tiene exactamente 23
    if (suma_a == 23 && suma_b == 23) {
        std::cout << "¡Ambos jugadores tienen 23! ¡Es un empate perfecto!" << std::endl;
        return;
    } else if (suma_a == 23) {
        std::cout << "¡Jugador A gana con exactamente 23 puntos!" << std::endl;
        return;
    } else if (suma_b == 23) {
        std::cout << "¡Jugador B gana con exactamente 23 puntos!" << std::endl;
        return;
    }

    // 1. Prioridad para números primos
    bool primo_a = esPrimo(suma_a);
    bool primo_b = esPrimo(suma_b);

    if (primo_a && !primo_b) {
        std::cout << "¡Jugador A gana con un número primo (" << suma_a << ")!" << std::endl;
        return;
    } else if (!primo_a && primo_b) {
        std::cout << "¡Jugador B gana con un número primo (" << suma_b << ")!" << std::endl;
        return;
    }

    // 3. Verificar quién está más cerca de 23 sin pasarse
    if (suma_a <= 23 && suma_b > 23) {
        std::cout << "Jugador B se pasó de 23. ¡Jugador A gana!" << std::endl;
        return;
    } else if (suma_b <= 23 && suma_a > 23) {
        std::cout << "Jugador A se pasó de 23. ¡Jugador B gana!" << std::endl;
        return;
    } else if (suma_a <= 23 && suma_b <= 23) {
        int distancia_a = 23 - suma_a;
        int distancia_b = 23 - suma_b;

        if (distancia_a < distancia_b) {
            std::cout << "¡Jugador A gana por estar más cerca de 23!" << std::endl;
        } else if (distancia_b < distancia_a) {
            std::cout << "¡Jugador B gana por estar más cerca de 23!" << std::endl;
        } else {
            std::cout << "¡Es un empate! Ambos jugadores están igual de cerca de 23." << std::endl;
        }
    } else {
        std::cout << "Ambos jugadores se pasaron de 23. ¡No hay ganador!" << std::endl;
    }
}

int main() {
    // Inicializar la semilla para los números aleatorios
    srand(static_cast<unsigned int>(time(0)));

    int suma_a = 0;
    int suma_b = 0;

    // Turno del Jugador A
    std::cout << "Turno del Jugador A\n";
    turnoJugador('A', suma_a);
    std::cout << std::endl;

    // Turno del Jugador B
    std::cout << "Turno del Jugador B\n";
    turnoJugador('B', suma_b);
    std::cout << std::endl;

    // Mostrar la suma total de ambos jugadores
    std::cout << "Suma total de los lanzamientos del Jugador A: " << suma_a << std::endl;
    std::cout << "Suma total de los lanzamientos del Jugador B: " << suma_b << std::endl;

    // Determinar el ganador basado en las condiciones
    determinarGanador(suma_a, suma_b);

    return 0;
}
