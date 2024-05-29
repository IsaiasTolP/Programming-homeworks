#include <iostream>

int main() {

    // El '\n' salta de línea pero no la limpia (Por cierto, esto es un comentario de una línea).
    
    /*
    En cambio el std::endl se toma su tiempo para limpiar el buffer al final, 
    lo que lo hace más lento, pero puede ser util, incluso necesario en algunos casos. El '\n' es mucho más rápido
    (Por cierto, esto es un comentario multilínea).
    */

    std::cout << "Hello World!" << '\n';
    std::cout << "Ahora en español" << std::endl;
    std::cout << "Hola Mundo!";

    return 0;
}