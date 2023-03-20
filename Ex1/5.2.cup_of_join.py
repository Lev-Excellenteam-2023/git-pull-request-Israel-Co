from functools import reduce


def all_list(tpl):
    """
    Check if the all elements in tpl are lists
    :param tpl: input tuple
    :return: True if all elements are list and False otherwise
    """
    list_bool = [isinstance(l, list) for l in tpl]
    return all(list_bool)


def join(*args, sep='-'):
    """
    Accepts an unlimited number of lists and joins them into one list
    and adds the <sep> between every two of them
    :param args: Tuple of lists
    :param sep: Char, use as a separator, default value for sep is '-'
    :return: One list that contains the whole elements of the lists, every two lists separated by sep
             and None if args is empty or some of elements in args are not list.
    """
    if all_list(args):
        try:
            return reduce(lambda l1, l2, s=sep: l1 + [s] + l2, args)
        except TypeError:
            return None

    return None

