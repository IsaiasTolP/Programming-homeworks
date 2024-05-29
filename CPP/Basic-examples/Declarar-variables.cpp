#include <iostream>

int main() {

    int x; //declaración de un número entero, X es la variable.
    x = 5; //Asignar la variable, debe guardar un entero porque eso fue lo que se declaró.
    /*
    También se puede asignar la variable directamente en una línea, si así lo deseamos:
    int x = 5; <----- De esa manera
    */
    int y = 6;
    int sum = x + y; // Una variable llamada sum que suma dos valores, fíjate que es una variable entera, por lo que ya sabemos que tipo de dato va a devolver.
    int flotante = 7.5; // ¿Y qué pasa, si ponemos un número no entero dentro de una variable entera? Pues nos devuelve solo la parte entera. ¡OJO! La parte entera, si es un 7.9, también da 7, NO se redondea.

    std::cout << x << '\n'; // Mostrar la variable.
    std::cout << y << '\n';
    std::cout << sum << std::endl;
    std::cout << flotante;

    return 0;
}