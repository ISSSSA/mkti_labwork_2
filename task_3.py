p, q = 2003, 2063
n = 4132189
target_values = [
    "18087**",
    "7142**",
    "2568**",
    "15934**",
    "22229**",
    "2806785"
]


def matches_pattern(value, pattern):
    str_value = str(value).zfill(len(pattern))
    if len(str_value) != len(pattern):
        return False
    return all(p == '*' or p == v for p, v in zip(pattern, str_value))


for x0 in range(1000, 10000):
    sequence = [x0]
    valid_sequence = True

    for i, pattern in enumerate(target_values):
        x_next = pow(sequence[-1], 2, n)
        if not matches_pattern(x_next, pattern):
            valid_sequence = False
            break
        sequence.append(x_next)
    if valid_sequence:
        break

ciphertext = "01010110101010011000010111001111"
x0 = 3769
n = 4132189
k = len(ciphertext)


def least_significant_bit(x):
    return x % 2


gamma = []
for i in range(1, 33):
    x_i = pow(x0, 2 ** i, n)
    gamma_bit = least_significant_bit(x_i)
    gamma.append(gamma_bit)
plaintext_bits = []

for c_bit, g_bit in zip(ciphertext, gamma):
    plaintext_bit = int(c_bit) ^ int(g_bit)
    plaintext_bits.append(str(plaintext_bit))

plaintext = ''.join(plaintext_bits)
print(sequence)
print("Расшифрованное сообщение:", int(plaintext, 2).to_bytes(4).decode('ascii'))
