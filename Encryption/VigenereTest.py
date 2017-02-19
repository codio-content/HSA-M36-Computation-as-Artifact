import VigenereCipher

msg = "Attack at dawn."
passphrase = "TANGO"

secret = VigenereCipher.encode(msg, passphrase)

print "Original Message", msg
print "Encrypted message:", secret

