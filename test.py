class Triplet:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
def string_for_csv(triplet):
        return str(triplet.a) + "," + str(triplet.b) + "," + str(triplet.c)

triplet = Triplet(10,10,10)
print(string_for_csv(triplet))
