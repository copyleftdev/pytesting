class Calculate(object):
  """docstring for Calculate"""
  def add(self,x , y):
    if type(x) == int and type(y) == int:
      return x + y
    else:
      TypeError("Invalid type: {} and {}".format(type(x),type(y)))

if __name__ == '__main__': #pragma: no cover
  calc = Calculate() #pragma: no cover
  result = calc.add(2,2) #rpagma: no cover
  print result  #pragma: no cover