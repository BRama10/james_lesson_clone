# functions

def function_name():
    print('ji')

def function_name(var1, var2):
    print(var1, var2)

def add(num1: int, num2: int) -> int:
    return num1 + num2

def add(num1: int, num2: int = 50) -> int:
    return num1 + num2


# def add() #if defaults
# def add(30, 50)
# def add(num1=30, num2=50)

# print(add(30, num2=50))

def position_unwrap(*the):
    print(the)
    print(type(the))


def add_all_numbers():
    """
    Pass in whatever numbers you want, and give the sum of them
    """

def keyword_unwrap(**kwargs):
    print(kwargs)

keyword_unwrap(a=5, b=6)

# position_unwrap('a', 'b', 'c', 'd')

def function_cool(name, *args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)


function_cool(
    'a', 'b', 'c',
    d='e', f='g'
)