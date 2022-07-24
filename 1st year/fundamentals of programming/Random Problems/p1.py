# Problem no. 1
# the function that checks whether a number is prime or not:
def isPrime(n):
    i = 2
    while i <= n // 2:
        if int(n % i) == 0:
            return False
        i += 1
    return True


# the main function where all the magic happens <3
def main():
    n = int(input("Input a natural number: "))
    if n < 2:
        print("The first prime number larger than your input is: ", 2)
    else:
        n += 1
        while isPrime(n) is False:
            n += 1
        print("The first prime number larger than your input is: ", n)


main()
