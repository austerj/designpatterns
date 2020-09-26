class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print('creating new object')
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


class ExampleSingleton(Singleton):
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    # prints "creating new object"
    A = ExampleSingleton(2)
    # prints nothing
    B = ExampleSingleton(3)
    # prints true; A and B are the same object
    print(A.__hash__() == B.__hash__())
