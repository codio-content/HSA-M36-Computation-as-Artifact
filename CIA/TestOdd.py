import ParodyCheck

number = "0111001"
number2 = ParodyCheck.makeOdd(number)

if ParodyCheck.checkEven(number2):
  print number2, "is even!"
else:
  print number2, "is odd!" # This is what we are hoping to get after having made the number have odd parody.
  