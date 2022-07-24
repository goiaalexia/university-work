# Problem no. 14
# the function that checks whether a number is prime or not:
def isPrime(n):
    i = 2
    while i <= n // 2:
        if int(n % i) == 0:
            return False
        i += 1
    return True


# the function that generates a list containing 1 if n is prime or
# a list containing the prime divisors of n if n is composed
def generatePrimeList(n):
    l = []
    if isPrime(n) is True:
        l.append(1)
        return l
    i = 2
    while n > 1:
        if int(n % i) == 0:
            l.append(i)
            while int(n % i) == 0:
                n //= i
        i = i + 1
    return l

 
# the main function where all the magic happens <3
def main():
    n = int(input("Input a natural number: \n"))
    print("The element of the sequence you're looking for is: ")
    if n < 4:
        return n
    n = n - 3
    currentNumber = int(4)
    while n > 0:
        l = generatePrimeList(currentNumber)
        i = int(0)
        for i in range(0, len(l)):
            if n - l[i] > 0:
                n = n - l[i]
            else:
                if isPrime(currentNumber) is False:
                    return l[i]
                else:
                    return currentNumber

        currentNumber = currentNumber + 1


print(main())
