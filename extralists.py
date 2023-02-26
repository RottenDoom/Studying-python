# Nice code I guess lists are the core of loops yeah.
import random


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    num = int(input("Enter a number :"))
    print([x for x in a if x <= num])


main()
