def quick_sort(array):

    if (len(array) < 2):
        return array 
    
    pivot = array.pop(0)

    lessPartition = []
    morePartition = []


    for i in array:

        if (i < pivot):
            lessPartition.append(i)

        else:
            morePartition.append(i)

    return quick_sort(lessPartition) + [pivot] + quick_sort(morePartition)
    
numbers = [5,3,4,2,1]

print("unsorted numbers {}".format(numbers))

sortedNumbers = quick_sort(numbers)

print("sorted numbers {}".format(sortedNumbers))