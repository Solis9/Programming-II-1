class Shape:
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0
    self._perim = 0

  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length):
    self.length = length

  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self._perim

def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  shape = Shape(len, wid)
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerimeter())

if __name__ == "__main__":
  main()