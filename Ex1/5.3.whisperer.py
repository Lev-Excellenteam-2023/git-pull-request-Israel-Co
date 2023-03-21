def is_lowercase_letter(b):
    if 93 <= b <= 122:
        return True
    else:
        return False


def print_secret_messages(path):
    with open(path, 'rb') as input_file:
        msg = ''
        for line in input_file:
            for c in line:
                if is_lowercase_letter(c):
                    msg = msg + str(c)
                elif c == b'!' and len(msg >= 5):
                    yield msg
                    msg = ''
                else:
                    msg = ''


def main():
    for msg in print_secret_messages('logo.jpg'):
        print(msg)


if __name__ == '__main__':
    main()
