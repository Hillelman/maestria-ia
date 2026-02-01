#include <iostream>
#include <omp.h>

int main() {
    std::cout << "Verificando la ejecucion de las directivas OMP!\n";

    #ifdef _OPENMP
        std::cout << "OpenMP disponible y funcionando" << std::endl;
    #endif

    return 0;
}
