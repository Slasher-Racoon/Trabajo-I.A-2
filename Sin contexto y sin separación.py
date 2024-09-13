#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

// Función para verificar si un número es primo
bool esPrimo(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= num / 2; ++i) {
        if (num % i == 0) return false;
    }
    return true;
}

// Función para lanzar un dado de 6 caras
int lanzarDado() {
    return rand() % 6 + 1;
}

// Función para manejar el turno de un jugador
int turnoJugador(string nombre) {
    int dado1 = lanzarDado();
    int dado2 = lanzarDado();
    int total = dado1 + dado2;
    bool dobles = (dado1 == dado2);
    
    cout << nombre << " lanza: " << dado1 << " y " << dado2 << " (Total: " << total << ")\n";

    // Verificar caso especial de dobles
    if (dobles) {
        cout << nombre << " ha sacado dobles (" << dado1 << "). ¿Desea dividir el lanzamiento y tirar 3 dados? (s/n): ";
        char opcion;
        cin >> opcion;

        if (opcion == 's' || opcion == 'S') {
            total = 0;  // Reiniciar el total
            for (int i = 0; i < 3; ++i) {
                int nuevoDado = lanzarDado();
                total += nuevoDado;
                cout << nombre << " lanza dado " << i + 1 << ": " << nuevoDado << " (Nuevo total: " << total << ")\n";
            }
        }
    }

    while (total < 23) {
        cout << nombre << ", ¿deseas lanzar un dado adicional? (s/n): ";
        char opcion;
        cin >> opcion;
        if (opcion == 's' || opcion == 'S') {
            int nuevoDado = lanzarDado();
            total += nuevoDado;
            cout << nombre << " lanza un dado: " << nuevoDado << " (Total actual: " << total << ")\n";

            if (total > 23) {
                cout << nombre << " se ha pasado de 23 y pierde.\n";
                return -1;
            }
        } else {
            break;
        }
    }

    return total;
}

// Función para determinar el ganador
void determinarGanador(int puntajeA, int puntajeB) {
    if (puntajeA == 23 && puntajeB != 23) {
        cout << "Jugador A gana con un puntaje exacto de 23.\n";
        return;
    } else if (puntajeB == 23 && puntajeA != 23) {
        cout << "Jugador B gana con un puntaje exacto de 23.\n";
        return;
    } else if (puntajeA == puntajeB && puntajeA == 23) {
        cout << "Ambos jugadores tienen un puntaje exacto de 23. Empate.\n";
        return;
    }

    if (puntajeA == -1 && puntajeB != -1) {
        cout << "Jugador A se ha pasado de 23. Jugador B gana.\n";
        return;
    } else if (puntajeB == -1 && puntajeA != -1) {
        cout << "Jugador B se ha pasado de 23. Jugador A gana.\n";
        return;
    } else if (puntajeA == -1 && puntajeB == -1) {
        cout << "Ambos jugadores se han pasado de 23. Nadie gana.\n";
        return;
    }

    if (esPrimo(puntajeA) && !esPrimo(puntajeB)) {
        cout << "Jugador A gana con un número primo (" << puntajeA << ").\n";
        return;
    } else if (esPrimo(puntajeB) && !esPrimo(puntajeA)) {
        cout << "Jugador B gana con un número primo (" << puntajeB << ").\n";
        return;
    }

    if (abs(23 - puntajeA) < abs(23 - puntajeB)) {
        cout << "Jugador A gana por estar más cerca de 23 (Puntaje A: " << puntajeA << ", Puntaje B: " << puntajeB << ").\n";
    } else if (abs(23 - puntajeB) < abs(23 - puntajeA)) {
        cout << "Jugador B gana por estar más cerca de 23 (Puntaje A: " << puntajeA << ", Puntaje B: " << puntajeB << ").\n";
    } else {
        cout << "Es un empate.\n";
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    cout << "Turno del Jugador A:\n";
    int puntajeA = turnoJugador("Jugador A");

    cout << "\nTurno del Jugador B:\n";
    int puntajeB = turnoJugador("Jugador B");

    cout << "\nResultado final:\n";
    determinarGanador(puntajeA, puntajeB);

    return 0;
}
