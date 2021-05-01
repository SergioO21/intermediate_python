def run():
    power_3_dict = {}

    # 1000 sqrt challenge
    sqrt_1000_dict = {i: i ** 0.5 for i in range(1, 1001)}

    # Dictionary comprehension form
    power_dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}

    # Common form
    for i in range(1, 101):
        if i % 3 != 0:
            power_3_dict[i] = i ** 3

    print(power_3_dict)
    print("")
    print(power_dict)
    print("")
    print(sqrt_1000_dict)


if __name__ == "__main__":
    run()
