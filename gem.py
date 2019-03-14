
class Gem:

    totalNumberOfGems = 0

    def __init__(self, nameIn = "%NO_INFO%", caratsNumberIn = 0, priceIn = 0, colorIn = "%NO_INFO%", weightIn = 0, purityIn = "%NO_INFO%"):
        self._name = nameIn
        self._caratsNumber = caratsNumberIn
        self._price = priceIn
        self._color = colorIn
        self._weight = weightIn
        self._purity = purityIn
    
    def __del__(self):
        print("%s was deleted" % self._name)

    def __str__(self):
        return "Name: {0}, Carats Number: {1}, Price: {2}\nColor: {3}, Weight: {4} kg, Purity: {5}.\n".format(self._name, self._caratsNumber, 
            self._price, self._color, self._weight, self._purity)

    @staticmethod
    def updateNumberOfGems(numberOfNewGems):
            Gem.totalNumberOfGems += numberOfNewGems




unknown = Gem()
aquamarine = Gem("Aquamarine", 10, 15, "Blue", 0.1, "Clear")

print(unknown)
print(aquamarine)

print("Total number of gems: " + str(Gem.totalNumberOfGems))
Gem.updateNumberOfGems(2)
print("Total number of gems: " + str(Gem.totalNumberOfGems))
print()