def adder(*args):
    sum = 0

    for n in args:
        sum = sum + n

    print("Sum: ", sum)


def intro(**kwargs):
    print("\nData type of argument:", type(kwargs))

    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com",
      Country="Wakanda", Age=25, Phone=9876543210)
