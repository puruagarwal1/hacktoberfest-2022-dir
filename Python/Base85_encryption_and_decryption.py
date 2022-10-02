#The base64 Module
#: Encoding and Decoding Base85
#This program demonstrates the encoding and decoding of BASE85 based Encoding.

print("Program that decrypts data using base85 function\n")

##The code starts from here
import base64

# Taking a string
_input = input("Enter the data: ")
# Encoding the string into bytes
bytOf_input = _input.encode("UTF-8")
# ASCII85 Encode the bytes
encodedBytes = base64.b85encode(bytOf_input)
print("The encrypted data in bytes: ",encodedBytes)
# Decoding the ASCII85 bytes to string
encry_str = encodedBytes.decode("UTF-8")
# Printing ASCII85 encoded string
print("The ASCII85 encrypted data is: ",encry_str)

"""-----------------------------------------------------------"""

# Encoding the ASCII85 encoded string into bytes
deco_bytOf_ = encry_str.encode("UTF-8")
# Decoding the ASCII85 bytes
decodedBytes = base64.b85decode(deco_bytOf_)
print("The decrypted data in bytes: ",decodedBytes)
# Decoding the bytes to string
decry_str = decodedBytes.decode("UTF-8")
print("The decrypted data is: ",decry_str)
