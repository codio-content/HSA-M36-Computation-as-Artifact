import ParodyCheck

number = "0111001"
number2 = ParodyCheck.makeEven(number)

if ParodyCheck.checkEven(number2):
  print number2, "is even!"
else:
  print number2, "is odd!" # This should not print unless something has gone wrong.
  