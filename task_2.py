irreducible_poly = 0x11b


def gf_multiply(x, y, mod=irreducible_poly):
    result = 0
    while y > 0:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & 0x100:
            x ^= mod
    return result


def matrix_vector_mult(matrix, vector):
    result = [0] * len(vector)
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] ^= gf_multiply(matrix[i][j], vector[j])
    return result


mix_columns_matrix = [
    [0x0b, 0x02, 0x01, 0x01],
    [0x01, 0x0b, 0x02, 0x01],
    [0x01, 0x01, 0x0b, 0x02],
    [0x02, 0x01, 0x01, 0x0b]
]

input_vector = [0x15, 0xab, 0x03, 0xf0]
mix_columns_result = matrix_vector_mult(mix_columns_matrix, input_vector)

print("Результат преобразования MixColumns:", [hex(x) for x in mix_columns_result])

inv_mix_columns_matrix = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]

inv_mix_columns_result = matrix_vector_mult(inv_mix_columns_matrix, mix_columns_result)

print("Результат обратного преобразования InvMixColumns:", [hex(x) for x in inv_mix_columns_result])
