alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
ceaser_offset = 3
ceaser_key = alphabet[ceaser_offset:] + alphabet[:ceaser_offset]
print(ceaser_key)

# Map msg with key
encrypt = lambda msg, key: ''.join(map(lambda c: key[alphabet.index(c)] if c in alphabet else c, msg.lower()))

decrypt = lambda msg, key: ''.join(map(lambda c: alphabet[key.index(c)] if c in alphabet else c, msg.lower()))


secret_message = "This is a secret message. 12349"

encrypted_message = encrypt(secret_message, ceaser_key)

decrypted_message = decrypt(encrypted_message, ceaser_key)

print(f"""
Origional Message: {secret_message},
Encrypted Message: {encrypted_message},
Decrypted Message: {decrypted_message}
Equal: {secret_message.lower() == decrypted_message}
""")
