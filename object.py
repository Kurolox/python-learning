class Bird():

    def __init__(self, name, eyes):
        self.name = name
        self.eyes = eyes

    def eyecount(self):
        print("Eyes: " + str(self.eyes))


mizu = Bird("Mizu",2)
print ("Testing " + mizu.name)
mizu.eyecount()
