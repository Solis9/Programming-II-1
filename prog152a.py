import sys
sys.setrecursionlimit(5000)

def fact(n):
  if n == 1:
    return n
  return n + fact(n-1)

def main():
  