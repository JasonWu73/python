from collections.abc import Iterable


def main():
    print(isinstance([1, 2, 3], Iterable))
    print(isinstance('hello', Iterable))
    print(isinstance(100, Iterable))


if __name__ == '__main__':
    main()
