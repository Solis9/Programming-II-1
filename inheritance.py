class Cat(Animal):
  def __init__(self, name, age, sound):
    super().__init__(name, age)
    self.sound = sound

  def saySound(self):
    print(self.sound)


cat = cat("Billy", 5, "Meow")
cat.sayHi()
cat.saySound()