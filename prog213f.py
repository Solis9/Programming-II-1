from Cl213f import *

def main():
  try:
    elecbill = []
    with open("data/prog213b.dat", 'r') as f:
      for line in f:
        kwh = float(line.strip())
        if kwh != -999:
          bill = Cl213f(kwh)
          elecbill.append(bill)
    for bill in elecbills:
      bill.calc()
      print(bill)
  except Exception as e:
    print("Error:", e)