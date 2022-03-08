import pickle


class Foo:
    attr = 'A class attribute'


pickle_string = pickle.dumps(Foo)
print(pickle_string)
