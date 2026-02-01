# COMPILANDO EN WINDOWS

- Ejecutar código unicamente en la terminal powershell (no en bash)
- Usar comando: `g++ test.cpp -o test.exe -fopenmp` (cambiar test.cpp por el nombre del archivo a compilar)
- El flag -fopenmp es necesario para habilitar las directivas de OpenMP
- Ejecutar el programa con: `.\test.exe`

# COMPILANDO EN MAC OS

- Ir al directorio del archivo a compilar
- En terminal: `g++-15 -fopenmp tarea1.cpp -o tarea1`
- Ejecutar el programa con: `./tarea1`
