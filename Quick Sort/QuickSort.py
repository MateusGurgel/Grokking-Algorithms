#8.225440979003906e-05
#0.00011038780212402344
#0.00011301040649414062

def quick_sort(array):

    if (len(array) < 2):
        return array 
    
    pivot = array[0]
    minors = [i for i in array[1:] if i <= pivot]
    bigger = [i for i in array[1:] if i > pivot]
    return quick_sort(minors) + [pivot] + quick_sort(bigger)
    
numbers = [5,3,4,2,1]

print("unsorted numbers {}".format(numbers))

sortedNumbers = quick_sort(numbers)

print("sorted numbers {}".format(sortedNumbers))
