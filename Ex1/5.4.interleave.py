from functools import reduce


def interleave(*args):
    """
    Get one or more iterables and interleave their elements.
    e.g. interleave('abc', [1, 2, 3], ('!', '@', '#')) -> ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    :param args: iterables input
    :return: List of the interleaved iterable's elements
    """
    zip_args = zip(*args)
    res = reduce(lambda tpl1, tpl2: list(tpl1) + list(tpl2), zip_args)
    return res


def generator_interleave(*args):
    """
    Generator, get one or more iterables and interleave their elements.
    :param args: iterables input
    :return: Generator that each round return list of the interleaved iterable's elements
    """
    # to avoid from index error
    lengths = [len(k) for k in args]
    min_len = min(lengths)

    res = []
    for i in range(min_len):
        res = res + [v[i] for v in args]
        yield res
