#include <iostream>
#include <omp.h>

// El siguiente código crea una región paralela y accesa al trabajo con hilos y procesamiento paralelo dentro de ella.
int main()
{
    std::cout << "Regiones paralelas!\n";
    int hilos, tid;

    // La creación de una región que puede ejecutar instrucciones en paralelo es muy sencilla en OpenMP,
    // solamente hay que llamar a la instrucción parallel de omp y pasarle de manera privada una variable
    // para controlar un id que corresponde con el proceso.
    #pragma omp parallel private(tid)
    {
        tid = omp_get_thread_num();
        std::cout << "Trabajando en el thread: " << tid << std::endl;

        // Solo el thread 0 (el principal) imprime el número de hilos que se están utilizando.
        if (tid == 0)
        {
            hilos = omp_get_num_threads();
            std::cout << "Numero de threads es: " << hilos << std::endl;
        }
    }
}
