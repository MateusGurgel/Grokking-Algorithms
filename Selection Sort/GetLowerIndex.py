def get_lower_index(array):
    lowerValue = array[0]
    Indexlower = 0

    for index, value in enumerate(array):
        if (value < lowerValue):
            lowerValue = value
            Indexlower = index
    
    return Indexlower
