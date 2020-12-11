byte = b'hello world'
print(type(byte))
print(byte)

def symbol_byte(letter):
    print(letter.encode('utf-8')[0])

def symbol_byte_ascii(letter):
    print(letter.encode('ascii')[0])

symbol_byte('a')
symbol_byte_ascii('e')

