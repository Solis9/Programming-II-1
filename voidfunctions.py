from calcfunctions import *
def doSomething():
  print("Hello, world!")

def printnums():
  x = 0
  while x < 10:
    print("x", x)
    x += 1


def main():
  doSomething()
  printnums()
  q, r = divmod2(5, 10)
  print(q, r)

if __name__ == "__main__":
  main()