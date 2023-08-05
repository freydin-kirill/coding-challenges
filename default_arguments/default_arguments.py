from abc import ABC, abstractmethod


class Stream(ABC):
    def __init__(self, number: int):
        self._number = number

    @abstractmethod
    def _eval(self, number: int):
        pass

    def get_next(self):
        for i in range(self._number):
            print(self._eval(i))


class EvenStream(Stream):
    def _eval(self, number: int):
        return 2 * number


class OddStream(Stream):
    def _eval(self, number: int):
        return 2 * number + 1


def print_from_stream(n, stream_name=None):
    if stream_name == "odd":
        stream = OddStream(n)
    else:
        stream = EvenStream(n)

    stream.get_next()


if __name__ == '__main__':
    for _ in range(int(input())):
        values = input().split()
        if len(values) == 2:
            print_from_stream(int(values[1]), values[0])
        else:
            print_from_stream(int(values[0]))


