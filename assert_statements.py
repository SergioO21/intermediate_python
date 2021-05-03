def cal_divisors(num):

    assert num > 0, "You can only enter positive numbers greater than 0"

    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    num = input("Enter a number: ")

    # This conditional is exclusive for negative numbers to send a different error
    if num[0] == '-':
        assert num[1:].isdigit(), "You can only enter one number"

    else:
        assert num.isdigit(), "You can only enter one number"

    print(cal_divisors(int(num)))


if __name__ == "__main__":
    run()
