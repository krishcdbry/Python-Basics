


class Krishcdbry:
   'Common base class for all Krishcdbrys'
   carCount = 0

   def __init__(self, name, cost):
      self.name = name
      self.cost = cost
      Krishcdbry.carCount += 1
   


   def displayKrishcdbry(self):
      print "Name : ", self.name,  ", cost: ", self.cost

car1 = Krishcdbry("Zara", 2000)

car2 = Krishcdbry("Manni", 5000)

car1.displayKrishcdbry()
car2.displayKrishcdbry()
