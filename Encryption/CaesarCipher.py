#CaesarCipher.py

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()                       # Convert all the letters in the message to uppercase.
    secret = ""
    
    for letter in message:
        if alpha.find(letter) >= 0:                 # make sure it is a letter.
            spot = (alpha.find(letter) + key) % 26  # wrap around the alphabet if we have passed Z.
            secret = secret + alpha[spot]           # build the secret message one letter at a time.
        else:
            secret = secret + letter                # the charactor was not a letter so it passes through unchanged.
    
    return secret                                   # return the encrypted message.

def decode(message, key):
    #implement a decode method that takes an encrypted message
    #and the key used to encrypt and returns the plaintext.
    return message

  
