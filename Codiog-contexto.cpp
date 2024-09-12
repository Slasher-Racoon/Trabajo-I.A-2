#include <iostream>
#include <random>
#include <ctime>
#include <cmath>

// Función que genera un número aleatorio entre 1 y 6, simulando un dado de 6 caras
int lanzarDado(std::mt19937& gen) {
    std::uniform_int_distribution<> distribucion(1, 6);
    return distribucion(gen);
}

// Función para verificar si un número es primo
bool esPrimo(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= std::sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

// Función que maneja el turno de un jugador, incluyendo la opción de lanzar dados adicionales
int turnoJugador(const std::string& jugador, std::mt19937& gen) {
    int dado1 = lanzarDado(gen);
    int dado2 = lanzarDado(gen);
    int suma = dado1 + dado2;

    std::cout << "Turno del jugador " << jugador << ":\n";
    std::cout << "Dado 1: " << dado1 << "\n";
    std::cout << "Dado 2: " << dado2 << "\n";

    // Verificamos si el jugador sacó dobles
    if (dado1 == dado2) {
        char opcionDividir = 'n';
        std::cout << "¡Sacaste dobles! ¿Deseas dividir tu lanzamiento y lanzar 3 dados adicionales por cada parte? (s/n): ";
        std::cin >> opcionDividir;

        if (opcionDividir == 's' || opcionDividir == 'S') {
            int sumaDiv1 = dado1;  // Primer grupo
            int sumaDiv2 = dado2;  // Segundo grupo

            // Lanzamos 3 dados adicionales para cada división
            std::cout << "Lanzando 3 dados adicionales para la primera división:\n";
            for (int i = 0; i < 3; ++i) {
                int dado = lanzarDado(gen);
                sumaDiv1 += dado;
                std::cout << "Dado " << i + 1 << ": " << dado << "\n";
            }
            std::cout << "Suma de la primera división: " << sumaDiv1 << "\n";

            std::cout << "Lanzando 3 dados adicionales para la segunda división:\n";
            for (int i = 0; i < 3; ++i) {
                int dado = lanzarDado(gen);
                sumaDiv2 += dado;
                std::cout << "Dado " << i + 1 << ": " << dado << "\n";
            }
            std::cout << "Suma de la segunda división: " << sumaDiv2 << "\n";

            // Elegimos la suma mayor de las dos divisiones como la suma final
            suma = std::max(sumaDiv1, sumaDiv2);
            std::cout << "Se elige la mayor suma entre las dos divisiones: " << suma << "\n";
        } else {
            std::cout << "Decidiste no dividir tu lanzamiento.\n";
        }
    }

    std::cout << "Suma inicial (sin división o tras división): " << suma << "\n";

    char opcion = 'n';
    while (suma <= 23) {
        std::cout << "Jugador " << jugador << ", ¿quieres lanzar un dado adicional? (s/n): ";
        std::cin >> opcion;

        if (opcion == 'n' || opcion == 'N') {
            break;  // Si el jugador no quiere lanzar otro dado, termina el turno
        }

        int dadoAdicional = lanzarDado(gen);
        suma += dadoAdicional;

        std::cout << "Dado adicional: " << dadoAdicional << "\n";
        std::cout << "Nueva suma total: " << suma << "\n";

        if (suma > 23) {
            std::cout << "¡La suma total supera 23! Fin del turno para el jugador " << jugador << ".\n";
            break;
        }
    }

    std::cout << "Suma final del jugador " << jugador << ": " << suma << "\n\n";
    return suma;
}

// Función para determinar el ganador basado en las reglas especificadas
void determinarGanador(int sumaA, int sumaB) {
    // Verificamos si algún jugador tiene exactamente 23
    if (sumaA == 23 && sumaB != 23) {
        std::cout << "El Jugador A gana con exactamente 23 puntos.\n";
        return;
    } else if (sumaB == 23 && sumaA != 23) {
        std::cout << "El Jugador B gana con exactamente 23 puntos.\n";
        return;
    } else if (sumaA == 23 && sumaB == 23) {
        std::cout << "Ambos jugadores tienen exactamente 23 puntos. ¡Empate!\n";
        return;
    }

    // Verificamos si ambos jugadores se pasaron de 23
    if (sumaA > 23 && sumaB > 23) {
        std::cout << "Ambos jugadores se pasaron de 23. ¡No hay ganador!\n";
        return;
    } else if (sumaA > 23) {
        std::cout << "El Jugador A se pasó de 23. El Jugador B gana.\n";
        return;
    } else if (sumaB > 23) {
        std::cout << "El Jugador B se pasó de 23. El Jugador A gana.\n";
        return;
    }

    // Verificamos los números primos
    bool primoA = esPrimo(sumaA);
    bool primoB = esPrimo(sumaB);

    if (primoA && !primoB) {
        std::cout << "El Jugador A gana con un número primo.\n";
        return;
    } else if (primoB && !primoA) {
        std::cout << "El Jugador B gana con un número primo.\n";
        return;
    } else if (primoA && primoB) {
        if (sumaA > sumaB) {
            std::cout << "Ambos jugadores tienen números primos. El Jugador A gana con un número primo más alto.\n";
        } else if (sumaB > sumaA) {
            std::cout << "Ambos jugadores tienen números primos. El Jugador B gana con un número primo más alto.\n";
        } else {
            std::cout << "Ambos jugadores tienen el mismo número primo. ¡Empate!\n";
        }
        return;
    }

    // Si ninguno tiene número primo, gana el que esté más cerca de 23
    if (abs(23 - sumaA) < abs(23 - sumaB)) {
        std::cout << "El Jugador A gana por estar más cerca de 23.\n";
    } else if (abs(23 - sumaB) < abs(23 - sumaA)) {
        std::cout << "El Jugador B gana por estar más cerca de 23.\n";
    } else {
        std::cout << "Ambos jugadores están a la misma distancia de 23. ¡Empate!\n";
    }
}

int main() {
    // Inicializamos el generador de números aleatorios
    std::random_device rd;
    std::mt19937 gen(rd()); // Mersenne Twister

    // Turno del Jugador A
    int sumaA = turnoJugador("A", gen);

    // Turno del Jugador B
    int sumaB = turnoJugador("B", gen);

    std::cout << "Resultados finales:\n";
    std::cout << "Suma final del Jugador A: " << sumaA << "\n";
    std::cout << "Suma final del Jugador B: " << sumaB << "\n\n";

    // Determinar el ganador
    determinarGanador(sumaA, sumaB);

    return 0;
}
