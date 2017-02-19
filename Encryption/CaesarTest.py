import CaesarCipher

msg = "Beware the ides of March"
key = 13

secret = CaesarCipher.encode(msg, key)
plaintext = CaesarCipher.decode(secret, key)

print "Original Message", msg
print "Encrypted message:", secret
print "Decrypted message:", plaintext    
