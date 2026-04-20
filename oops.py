class car:
  def __init__ (self,brand,color):
    self.Brand = brand
    self.Color = color


  def start_engine(self):
    print(f"{self.Brand} engine started")

car1 = car("tata","black")
car1.start_engine()