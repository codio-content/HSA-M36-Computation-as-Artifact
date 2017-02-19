import CaesarCipher

def encode(message, password):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()                       # Convert all the letters in the message to uppercase.
    password = password.upper()
    secret = ""
    
    index = 0
    while index < len(message):
      letter = message[index]
      passLetter = password[index % len(password)]  #Use the password letter as the key.  Password is shorter than message so it will be re-used
      key = alpha.find(passLetter)
      secret = secret + CaesarCipher.encode(letter, key) #Use the original Caesar Cipher with our rotating key.
      index += 1
 
    return secret                                   # return the encrypted message.

