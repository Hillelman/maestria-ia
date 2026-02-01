#include <iostream>
#include <omp.h>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;
const int SIZE = 1000000;

void llenarArreglo(vector<int>& arr) {
    for (int i = 0; i < SIZE; ++i) {
        arr[i] = rand() % 100; // Números aleatorios entre 0 y 99
    }
}

void sumarArreglos(vector<int>& arr1, vector<int>& arr2, vector<int>& resultado) {
    #pragma omp parallel for num_threads(2)
    for (int i = 0; i < SIZE; ++i) {
        resultado[i] = arr1[i] + arr2[i];
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0))); // Semilla para números aleatorios

    vector<int> arreglo1(SIZE);
    vector<int> arreglo2(SIZE);
    vector<int> resultado(SIZE);

    llenarArreglo(arreglo1);
    llenarArreglo(arreglo2);
    sumarArreglos(arreglo1, arreglo2, resultado);

    cout << "Total de elementos: " << SIZE << "\n" << endl;
    cout << "Primeros 10 resultados de la suma:\n" << endl;
    for (int i = 0; i < 10; ++i) {
        cout << arreglo1[i] << " + " << arreglo2[i] << " = " << resultado[i] << endl;
    }

    return 0;
}
