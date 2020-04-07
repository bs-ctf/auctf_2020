'''
Base 64 encoded
'''

import base64

encoded_text="YXVjdGZ7NExMX3kwVXJfQjQ1M19SX2IzbDBOZ18yX3VTXzEyNGRmMnNkYXN2fQ=="
plaintext=base64.b64decode(encoded_text)
print(plaintext)