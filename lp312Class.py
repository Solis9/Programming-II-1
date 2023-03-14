class ClLP312:
  def __init__(self, fd, cg, et, rt):
    self.food = fd
    self.clothing = cg
    self.entertainment = et
    self.rent = rt
    self.budget = 0
    self.percents = [0]*4

  def _percent(self, number):
    return round((number / self.budget) * 100, 2)

  def calculate(self):
    self.budget = self.food + self.clothing + \
                  self.entertainment + self.rent
    self.percent[0] = self._percent(self.food)
    self.percent[1] = self._percent(self.clothing)
    self.percent[2] = self._percent(self.entertainment)
    self.percent[3] = self._percent(self.rent)

  def display(self):
    print("Category\tBudget")
    print(f"Food\t\t\t{self.percent[0]}%")
    print(f"Clothing\t\t{self.percent[1]}%")
    print(f"Entertainment\t\t{self.percent[2]}%")
    print(f"Rent\t\t\t{self.percent[3]}%")


def main():
  print("Enter the amount spent last moth on the following items: \n")
  food = float(input("Food: $"))
  clothing = float(input("Clothing: $"))
  entertainment = float(input("Entertainment: $"))
  rent = float(input("Rent: $"))
  print()

  budget = ClLP312(food, clothing, entertainment, rent)
  budget.calculate()
  budget.display()


if __name__ == "__main__":
  main()