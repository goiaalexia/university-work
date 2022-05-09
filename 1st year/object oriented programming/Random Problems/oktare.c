#pragma clang diagnostic push
#pragma ide diagnostic ignored "cert-err34-c"

/* PROBLEM STATEMENT #2:
a. Generate the first n prime numbers (n is a given natural number).
b. Given a vector of numbers, find the longest contiguous subsequence
 such that any two consecutive elements are relatively prime. */

#include <stdio.h>

struct Tuple {
    int a;
    int b;
};

void read_vector(int n, int vector[]) {
    for (int i = 0; i < n; i++) {
        printf("\nv[%d]= ", i);
        scanf("%d", &vector[i]);
    }
}

int is_relatively_prime(int a, int b) { // USING EUCLID'S ALGORITHM
    while (a != b) {
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }
    return a;
}

int is_prime(int n) {
    int d = 2;
    if (n == 1)
        return 0;
    if (n == 2)
        return 1;
    while (d * d <= n) {
        if (n % d == 0) {
            return 0;
        }
        d++;
    }
    return 1;
}

// LAB 2 ACTIVITY (STATEMENT 3)
int prime_number_exponent(int n, int p) {
    int exponent = 0;
    while (n != 0 && n % p == 0) {
        n /= p;
        exponent++;
    }
    return exponent;
}

void generate_prime_numbers(int n) {
    int counter = 0, number = 1;
    if (n < 0) {
        return;
    }
    while (counter != n) {
        if (is_prime(number) == 1) {
            printf("%d ", number);
            counter++;
        }
        number++;
    }
}

struct Tuple longest_subsequence(int len, int vector[]) {

    int start, final = 0, i = 0, max_len = 0, current_len = 0, good_start = 0, good_final = 0;
    while (i < len - 1) {
        start = i;
        while (vector[i + 1] != 0 && vector[i] != 0 && is_relatively_prime(vector[i], vector[i + 1]) == 1) {
            final = i + 1;
            i++;
            current_len++;
        }
        if (current_len > max_len) {
            max_len = current_len;
            good_final = final;
            good_start = start;
        }
        i++;
    }
    struct Tuple tup;
    tup.a = good_start;
    tup.b = good_final;
    return tup;
}

void exit_program(int *running) {
    *running = 0;
}

// heyo comment line

int main() {
    printf("Welcome to the first assignment!\n");
    int running = 1, option = 0, length, number, vector[1000] = {0}, n = 0, p = 1;
    struct Tuple tup;
    while (running == 1) {
        printf("-- OPTIONS --\n1. Read a vector of numbers from the console\n2. First problem\n3. Second problem\n4. Exit\n5. Lab 2 Functionality");
        printf("\n\nOption (number between 1-5): ");
        scanf("%d", &option);
        switch (option) {
            case 1: // VECTOR READING
                printf("\nNumber of integers to be read for the vector: ");
                scanf("%d", &length);
                read_vector(length, vector);
                break;
            case 2: // FIRST PROBLEM (2)
                printf("\nNumber of prime numbers to be printed: ");
                scanf("%d", &number);
                printf("\nPrime numbers: ");
                generate_prime_numbers(number);
                break;
            case 3: // SECOND PROBLEM (2)
                tup = longest_subsequence(length, vector);
                printf("\nLongest contiguous subsequence such that any two consecutive elements are relatively prime is determined by %d, %d\n",
                       tup.a, tup.b);
                break;
            case 4: // EXIT
                exit_program(&running);
                break;
            case 5: // LAB 2 FUNCTIONALITY (Print the exponent of a prime number p from the decomposition in prime
                // factors of a given number n (n is a non-null natural number).
                while (n == 0) {
                    printf("\nNumber to be decomposed:");
                    scanf("%d", &n);
                }
                while (is_prime(p) == 0) {
                    printf("\nPrime (!) number p whose exponent needs to be found:");
                    scanf("%d", &p);
                }
                printf("Exponent: %d\n", prime_number_exponent(n, p));
                break;
            default:
                printf("Please input a valid option!\n");
                break;
        }
    }
    printf("\nGoodbye!");
    return 0;
}