def run():
    
    squares = []
    squares3 = []
    squares469 = [i for i in range(1, 100000) if i % 36 == 0 and len(str(i)) < 6]

    for i in range(1, 101):
        squares.append(i ** 2)

    for i in range(1, 101):
        if i % 3 != 0:
            squares3.append(i ** 2)
    
    print(squares)
    print("")
    print(squares3)
    print("")
    print(squares469)

if __name__ == "__main__":
    run()