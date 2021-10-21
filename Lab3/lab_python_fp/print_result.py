def print_result(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return_value = func(*args, **kwargs)

        if isinstance(return_value,list):
            for i in return_value:
                print(i)
                
        elif isinstance(return_value, dict):
            for i in return_value:
                print(i, "=", return_value[i])
        else:
            print(return_value)

        return return_value
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
