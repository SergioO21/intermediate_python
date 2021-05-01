def run():

    # To use reduce
    from functools import reduce

    # With list comprehensions
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = [i for i in my_list if i % 2 != 0]
    print("With list comprehensions = {}".format(odd))

    # With filter function
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda i: i % 2 != 0, my_list))
    print("With filter function = {}".format(odd))

    print("-----------------------------------------------------------")

    # With list comprehensions
    my_list = [1, 2, 3, 4, 5]
    squares = [i ** 2 for i in my_list]
    print("With list comprehensions = {}".format(squares))

    # With map function
    my_list = [1, 2, 3, 4, 5]
    squares = list(map(lambda i: i ** 2, my_list))
    print("With map function = {}".format(squares))

    print("-----------------------------------------------------------")

    # With for loop
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = 1

    for i in my_list:
        all_multiplied = all_multiplied * i

    print("With a for loop = {}".format(all_multiplied))

    # With reduce function
    my_list = [2, 2, 2, 2, 2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print("With reduce function = {}".format(all_multiplied))


if __name__ == "__main__":
    run()
