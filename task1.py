old_ciphertext = bytes.fromhex("5f991ecef9c68bd0460c90ac68726f9c984c0f38fc7b750f7fd5a8789e521b645e9d3c82f4b096540318491d23f8d429599b7663ad4bc4fec02186136f3630b4d1a817cbef838dd00a244ba914e8a55d61c8cd4d00d4d7a560bd71d41b91a3117a46ba005e073aca14e7f36f90dec63bb5ddd4217e244839c23ed12b0990261507dbc98386ab90f1021665e3d03030503da21035197d09f4f8")
known_plaintext = b"Hi Alice, this is Bob. To work on our website, you need to log in to the administration panel. The login credentials are provided in the following email."
new_ciphertext = bytes.fromhex(" 54825bebf0c19cdc0b4097e4676e3dd584193f77ed3c213e3ed58a64894b556a5dd869d7e7f48c580f47001927a78727599c3237e85dc5bdc62bd21169384faddefa0cc8")

key_stream = bytes([c ^ p for c, p in zip(old_ciphertext, known_plaintext)])
decrypted_message = bytes([c ^ k for c, k in zip(new_ciphertext, key_stream)])

print("Расшифрованное сообщение:", decrypted_message.decode('utf-8', errors='ignore'))