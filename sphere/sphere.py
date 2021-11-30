import math, pickle

class Sphere(object):

    def __init__(self, radius):
        # *** STEP 1 ***
        # uncomment the following line
        self.radius = radius
        pass

    # *** STEP 2 ***
    # uncomment the following 2 lines
    #def __str__(self):
    #    return '%s(%s)' % (self.__class__.__name__, self.radius)

    def surface(self):
        # *** STEP 3 ***
        # uncomment the following line
        #return 4.0 * 3.1416 * self.radius ** 2
        pass

    def volume(self):
        # *** STEP 4 ***
        # uncomment the following line
        #return 4/3 * 3.1416 * self.radius ** 3
        pass

    def diameter(self):
        # *** STEP 5 ***
        # uncomment the following line
        #return self.radius
        pass

    def dump(self, filename):
        # *** STEP 6 ***
        # uncomment the following 2 lines
        #with open(filename, "w") as f:
        #    pickle.dump(self, f)
        pass

def loadSphere(filename):
    # *** STEP 7 ***
    # uncomment the following 3 lines
    #with open(filename, "r") as f:
    #    sphere = pickle.load(f)
    #    return sphere
    pass
