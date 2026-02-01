#include <iostream>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

#define N 24
using namespace std;

int tid;

// El siguiente código permite definir el número de hilos que se desean utilizar en una región paralela.
int main()
{
    cout << "Estableciendo la cantidad de Hilos!\n";
    int nHilos;

    cout << "Cuantos hilos quieres trabajar: ";
    cin >> nHilos;

    #ifdef _OPENMP
        omp_set_num_threads(nHilos);
    #endif

    // Crear una región paralela
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        cout << "El thread " << tid << " esta en marcha " << endl;
        cout << "El thread " << tid << " ha terminado " << endl;
    }
}
