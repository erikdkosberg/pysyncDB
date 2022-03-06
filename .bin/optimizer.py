class Op():
    def __init__(self):
        self.name = "Optimization Library"
        self.path = Op.__dir__(self)
        #self.size = Op.__sizeof__(Op().path)
    def exec_time(self):
        pass
    def cPy(self):
        pass
    def reorder(self):
        pass
    def __repr__(self):
        pass
    def archive_the_bad_stuff(self):
        """
        Throws everything that doesn't make sense to the optimizer into some archive text file that
        we can throw onto our DB somewhere.

        """
        pass

t = Op()
print(t.path)

out = [z for z in range(10)]

#Profile("[z for z in range(10)]")
