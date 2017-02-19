#ParodyCheck.py
#Uses a leading bit to check for parity

#takes a 7-bit String and converts it to an even parity
#adds a leading 0 or 1 to the front of the String to ensure
#the result has even parity. 
def makeEven(number):
  parody = 0
  for digit in number:
    if digit == '1':
      parody = parody + 1
      
  
  if parody % 2 == 0:
    return '0' + number
  
  else:
    return '1' + number

  
#takes a 7-bit String and converts it to an even parity
#adds a leading 0 or 1 to the front of the String to ensure
#the result has even parity. 
def makeOdd(number):
  #needs to be implemented
  return number 


def checkEven(number):
  parody = 0
  for digit in number:
    if digit == '1':
      parody = parody + 1
     
  return parody % 2 == 0

def checkOdd(number):
  #needs to be implemented
  return False

