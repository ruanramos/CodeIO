def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    soma = 0
    for i in range(len(array)):
        if i % 2 == 0:
            soma += array[i]

    print(soma)
            
    if not array:
       return 0
    return soma * array[-1]
