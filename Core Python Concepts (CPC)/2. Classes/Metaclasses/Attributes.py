class Meta(type):
    def __getattribute__(*args):
        print("Metaclass getattribute invoked")
        return type.__getattribute__(*args)


class C(object, metaclass=Meta):
    def __len__(self):
        return 10

    def __getattribute__(*args):
        print("Class getattribute invoked")
        return object.__getattribute__(*args)


c = C()
c.__len__()  # Explicit lookup via instance
type(c).__len__(c)  # Explicit lookup via type
len(c)  # Implicit lookup
