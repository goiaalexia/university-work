# Problem no. 7
# the function that checks whether a number is prime or not:
def isPrime(n):
    i = 2
    while i <= n // 2:
        if int(n % i) == 0:
            return False
        i += 1
    return True


# the function that finds a prime greater than a given number n:
def findGreaterPrime(n):
    p = n + 1
    if p < 2:
        return 2
    while isPrime(p) is False:
        p += 1
    return int(p)


# the main function where all the magic happens <3
def main():
    n = int(input("Input a natural number: "))
    p1 = findGreaterPrime(n)
    p2 = findGreaterPrime(p1)
    while p2 - p1 != 2:
        p1 = p2
        p2 = findGreaterPrime(p1)
    print("The twin numbers immediately larger than your input are: ", p1, " & ", p2)


main()
