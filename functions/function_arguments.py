#/usr/in/python3


def main():
    test_simple_args(400)
    test_default_args(400, 900)
    test_list_args(3, 4, 5, 6, 7)
    test_kwargs(name = 'Jon', age = 28, id = 645343)
    test_combined_args(1, 2 , 3, 4, 5, 6, name = 'Jon', age = 28, id = 645343)
    

def test_simple_args(simple):
    print('This is Function with simple arguments: ', simple)

def test_default_args(simple, other = 40, another = None):
    print('This is a function with default argumets: ', simple, other, another)
def test_list_args(*args):
    print('This is a function with list arguments stored in *args : ', args)

def test_kwargs(**kwargs):
    print('This is a function with Named arguments: ', kwargs)

def test_combined_args(sample_1, sample_2, *args, **kwargs):
    print('This is a function with combined arguments: ',sample_1, sample_2, args, kwargs)


if __name__ == "__main__":
    main()