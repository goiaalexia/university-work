import random


def generate_number():
    """
    the function generates the random secret number by firsly generating the first digit, and then getting
    the last 3 digits from the left digits. it cannot generate the cheat code!
    :return: the randomly generated number
    """
    while True:
        num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        final_number = random.randint(1, 9)
        num_list.pop(final_number)
        last_three = random.sample(num_list, 3)
        final_number *= 1000
        final_number += last_three[0] * 100 + last_three[1] * 10 + last_three[2]
        if final_number == 8086:
            continue
        return final_number


def check_distinct_digits(n):
    l = []
    while n != 0:
        l.append(n % 10)
        n /= 10
    for i in range(0, 3):
        for j in range(i + 1, 4):
            if l[i] == l[j]:
                return False
    return True


def codes(number, guessed_number):
    cnumber = number
    cguessed_number = guessed_number
    code_numb = 0
    for i in range(0, 4):
        if cguessed_number % 10 == cnumber % 10:
            code_numb += 1
        cguessed_number /= 10
        cnumber /= 10
    return code_numb

def runners(number, guessed_number):
    cnumber = number
    cguessed_number = guessed_number
    runner_number = 0
    list1 = []
    list2 = []
    for i in range(0,4):
        list1.append(int(cguessed_number %10))
        list2.append(int(cnumber % 10))
        cguessed_number /= 10
        cnumber /= 10
    for i in range(0,4):
        for j in range(0,4):
            if i != j and list1[i] == list2[j]:
                runner_number += 1
    return runner_number
