
def test_func(msg=None):
    if msg is None:
        print('Nothing to print')
    else:
        print(msg)


if __name__ == '__main__':
    to_print = 'Hello'
    test_func(to_print)
