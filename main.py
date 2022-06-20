import itertools

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
    [],
    ['w', ['x', 'y', 'z']]
]

n_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]


class FlatIterator:
    def __init__(self, nst_list):
        self.n_list = nst_list
        self.cursor = 0
        self.flat_list = []
        i = 0
        j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.n_list):
            if not isinstance(self.n_list[self.cursor], list):
                self.cursor += 1
                return self.n_list[self.cursor - 1]
            else:
                self.n_list = list(self.n_list[self.cursor]) + self.n_list[self.cursor + 1:]
                self.cursor = 0
                return self.__next__()
        else:
            raise StopIteration


def flat_generator(nst_list):
    cursor = 0
    while cursor < len(nst_list):
        if not isinstance(nst_list[cursor], list):
            yield nst_list[cursor]
            cursor += 1
            nst_list[cursor - 1]
        else:
            nst_list = list(nst_list[cursor]) + nst_list[cursor + 1:]
            cursor = 0


if __name__ == '__main__':

    # Итератор
    print('Итератор')
    for item in FlatIterator(nested_list):
        print(item)
    print('')

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('')

    # Генератор
    print('Генератор')
    for item in flat_generator(nested_list):
        print(item)
    print('')

    # Вариант с itertools
    print('Вариант с itertools')
    flat_list = list(itertools.chain.from_iterable(n_list))
    print(flat_list)
