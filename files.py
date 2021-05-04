def read():
    numbers = []
    # Parameter "r" to only read a file
    with open("./numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)


def write():
    names = ["Alberto", "José", "Pablo", "Marcelo", "Pedro"]
    # with = prevents the file from breaking if the program closes unexpectedly
    # Parameter "w" to write or rewrite text in a file
    with open("./names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def write_append():
    names = ["María", "Daniela", "Lucía", "Danna", "Andrea"]
    # Parameter "a" to append text in a file
    with open("./names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()
    write_append()


if __name__ == "__main__":
    run()
