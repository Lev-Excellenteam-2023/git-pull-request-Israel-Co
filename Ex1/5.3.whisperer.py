SIZE = 5


def print_secret_messages(path):
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
    for msg in print_secret_messages('logo.jpg'):
        print(msg)


if __name__ == '__main__':
    main()
