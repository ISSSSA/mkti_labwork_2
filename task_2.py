import numpy as np

# Неприводимый многочлен для поля F_2^8
MOD_POLY = 0x11b  # x^8 + x^4 + x^3 + x + 1


# Функция для умножения в поле F_2^8
def gf_multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:  # если старший бит установлен
            a ^= MOD_POLY
        b >>= 1
    return result & 0xff  # возврат только младших 8 бит


# Определение матрицы MixColumns для c(x) = α·x^3 + x^2 + x + (α^3 + α + 1)
# Для удобства будем считать α = 0x02 (как в стандартном AES)
alpha = 0x02
alpha3 = gf_multiply(gf_multiply(alpha, alpha), alpha)  # α^3

mix_columns_matrix = np.array([
    [alpha, 1, 1, alpha3 ^ alpha ^ 1],
    [alpha3 ^ alpha ^ 1, alpha, 1, 1],
    [1, alpha3 ^ alpha ^ 1, alpha, 1],
    [1, 1, alpha3 ^ alpha ^ 1, alpha]
], dtype=int)

# Вектор, к которому применяется MixColumns
vector = np.array([0x15, 0xab, 0x3, 0xf0], dtype=int)


# Функция для умножения матрицы на вектор в поле F_2^8
def mix_columns(matrix, vector):
    result = np.zeros(4, dtype=int)
    for i in range(4):
        for j in range(4):
            result[i] ^= gf_multiply(matrix[i][j], vector[j])
    return result


# Применение MixColumns
result_vector = mix_columns(mix_columns_matrix, vector)
print("Результат применения MixColumns:", result_vector)

# Матрица для InvMixColumns, обратная к матрице MixColumns
# Эта матрица вычислена на основе обратного многочлена.
# Предположим, что обратный многочлен имеет нужные коэффициенты:
inv_mix_columns_matrix = np.array([
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
], dtype=int)


# Функция для применения InvMixColumns
def inv_mix_columns(matrix, vector):
    result = np.zeros(4, dtype=int)
    for i in range(4):
        for j in range(4):
            result[i] ^= gf_multiply(matrix[i][j], vector[j])
    return result


# Применение InvMixColumns к результату MixColumns
original_vector = inv_mix_columns(inv_mix_columns_matrix, result_vector)
print("Результат применения InvMixColumns:", original_vector)
