def sort(array):
    # len irá retornar a quantidade de elementos
    # Percorrendo da posição zero a posição final
    for p in range(0, len(array)):

        while p > 0:
            # p - 1 representa a posição anterior
            # e verificando se é maior que a posição atual
            if array[p - 1] > array[p]:
                # Realizando a troca
                array[p], array[p - 1]  = array[p - 1], array[p]
            p -= 1

array = [9, 7, 8, 1, 3, 5, 2, 0]
copy_array = array[:]
sort(array)
print(array)