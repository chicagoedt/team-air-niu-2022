import numpy as np

class MyClass:
    classVar = np.arange(0, 5, 0.5)

    def __init__(self):
        self.name = "george"
        self.location = "town"

    @classmethod
    def setClassVar(self):
        self.classVar = np.arange(0,10,1)
