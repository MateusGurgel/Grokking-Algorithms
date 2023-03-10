from GetLowerIndex import get_lower_index

def selection_sort(array):
    
    arraySize = len(array)
    sortedArray = []

    for i in range(arraySize):

        lowerIndex = get_lower_index(array)
        lowerValue = array.pop(lowerIndex)
        sortedArray.append(lowerValue)
    
    return sortedArray


numbers = [4,3,6,1,2,5]

print("unsorted numbers {}".format(numbers))

sortedNumbers = selection_sort(numbers)

print("sorted numbers {}".format(sortedNumbers))
