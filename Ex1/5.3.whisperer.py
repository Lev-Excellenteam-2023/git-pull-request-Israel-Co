# const vars
SIZE = 5
PATH = 'resources/logo.jpg'


def print_secret_messages(path):
    """
    opening a file as binary, scanning it to find encoded messages.
    The messages are lowercase alphabetical, at least 5 letters long and finish in exclamation mark <'!'>.
    :param path: Path to the file
    :return: Generator that return an decoded message each round
    """
    res = ''
    with open(path, 'rb') as input_file:
        while True:
            c = input_file.read(1)
            if not c:
                break
            if c.islower():
                res += c.decode()
            elif c == b'!':
                if len(res) >= SIZE:
                    yield res
                    res = ''
            else:
                res = ''


def main():
    for msg in print_secret_messages(PATH):
        print(msg)


if __name__ == '__main__':
    main()
