def cal_divisors(num):
    divisors = []

    try:
        if num <= 0:
            raise ValueError("You can only enter positive numbers greater than 0")

        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors

    except ValueError as ve:
        print(ve)


def run():

    try:
        num = int(input("Enter a number: "))
        print(cal_divisors(num))

    except ValueError:
        print("You can only enter one number")


if __name__ == "__main__":
    run()
