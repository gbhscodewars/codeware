import math
def factorial(n):
  if n == 0:
    return 1;
  else:
    return n * factorial(n-1)
 
def vector(magnitude, degrees):
  radians = (degrees * math.pi)/180
  componentx = magnitude * (math.sin(radians))
  componenty = magnitude * (math.cos(radians))
  print(componentx)
  print(componenty)
  
