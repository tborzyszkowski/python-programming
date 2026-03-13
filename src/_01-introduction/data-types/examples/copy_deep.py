import copy

macierz = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'], ]
print(macierz)

macierz_copy = copy.copy(macierz)  # płytka kopia (shallow copy)
macierz_copy[0][0] = 'z'
print(macierz_copy)
print(macierz)
print('======')
macierz_deepcopy = copy.deepcopy(macierz)
macierz_deepcopy[0][0] = 'q'
print(macierz_deepcopy)
print(macierz)

