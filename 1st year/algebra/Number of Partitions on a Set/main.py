import math
import itertools
from mit import more_itertools

"""
1. For computing the number of partitions of a set with n elements, we can use
Dobinski's formula. Not gonna lie, I tried implementing a solution with the Bell's
triangle, but I couldn't manage to. This is an easier method. Researched this method online.
Dobinski's formula: the sum from k=1 to n of k^n/k! , multiplied by 1/e.
"""
f = open('number.txt', 'r', encoding='utf-8')
g = open('result.txt', 'w', encoding='utf-8')


def bell_number(n):
    n = int(n)
    s = 0
    iterations = 100  # number for precision
    for i in range(0, iterations):
        power = math.pow(i, n)
        fact = math.factorial(i)
        s += power / fact
    return int(round(s / math.e))


def print_partition_number(n):
    n = int(n)
    if n == 1:
        print("1. The number of partitions on a set A = { a1 }  is 1\n", file=g)
    elif n == 2:
        print("1. The number of partitions on a set A = { a1 , a2 }  is ", bell_number(2), file=g)
    elif n == 3:
        print("1. The number of partitions on a set A = { a1 , a2 , a3 }  is ", bell_number(3), file=g)
    else:
        n = str(n)
        stringy = "a" + n
        print("1. The number of partitions on a set A = { a1 , ... ,", stringy, " }  is ", bell_number(n), file=g)


"""
    We are going to be printing the equivalence relations for the partitions in descending order.
    We are going to start from the most fragmented partition and work our way down, in numerical order
    for the next ones. I will not notate them, but as an example, for n = 3, they will go like this:
    {{a1},{a2},{a3}}
    {{a1,a2},{a3}}
    {{a1,a3},{a2}} 
    {{a2,a3},{a1}}
    {{a1,a2,a3}}
"""


def get_combinations(l):
    """
    function that gets all the relation combinations possible. researched this method online.
    :param l: the list of relations
    :return: the combinations
    """
    for i, j in itertools.combinations(range(len(l) + 1), 2):
        yield l[i:j]


def partitions(n):
    """
    function that prints the partition's relations of a number n
    :param n: the number
    :return: no return, it prints the relations in descending order, as described above
    """
    element_list = []
    for i in range(1, n + 1):
        ci = str(i)
        element_list.append("a" + ci)
    relation_matrix = []
    for i in range(0, n):  # building the matrix that contains all the possible relations between partition elements
        for j in range(i + 1, n):
            if i != j:  # not adding the identical relations
                relation_matrix.append([[element_list[i], element_list[j]], [element_list[j], element_list[i]]])
    if n == 1:
        print("[a1] ⇝ ∆A", file=g)
    if n == 2:
        print("[[a1],[a2]] ⇝ ∆A")
        print("[[a1,a2]] ⇝ A x A", file=g)
    elif n != 1:  # general case
        c = int(2)
        b = bell_number(n)
        partition_list = [
            [part for k in range(1, len(element_list) + 1) for part in more_itertools.set_partitions(element_list, k)]]
        j = 1
        for i in sorted(get_combinations(relation_matrix), key=len):  # we get the combinations, however, if we wanna
            # display in descending order we need to sort them. also researched this certain method online.
            if c < b:  # we display numbers until we reach bell's number which is the last relation.
                print(partition_list[0][j], "⇝ ∆A u", file=g)
                j += 1
                c += 1
        print(b, "⇝ A x A", file=g)


def print_relations(n):
    if n <= 8:
        print("2. The equivalence relations on set A for n =", n, "is: \n", file=g)
        partitions(n)


def start():
    n = int(f.read())
    print_partition_number(n)
    print_relations(n)


start()
