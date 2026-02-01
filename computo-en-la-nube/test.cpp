#include <omp.h>
#include <iostream>

int main() {
    #pragma omp parallel
    {
        #pragma omp single
        std::cout << "Hilos: " << omp_get_num_threads() << "\n";
    }
}
