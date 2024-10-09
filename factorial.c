#include <stdio.h>

int factorial_iterativo(int n) {
    int factorial = 1;
    for (int i = 2; i <= n; ++i) {
        factorial *= i;
    }
    return factorial;
}

int main() {
    int num;
    printf("Ingrese un número: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("El factorial no está definido para números negativos.\n");
    } else {
        printf("El factorial de %d es: %d\n", num, factorial_iterativo(num));
    }

    return 0;
}