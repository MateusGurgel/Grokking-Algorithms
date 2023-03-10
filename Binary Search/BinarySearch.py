def binary_search(list, item):
    lowerValue = 0
    higherValue = len(list) - 1
    attempts = 0

    while lowerValue <= higherValue:
        midValue = (lowerValue + higherValue) // 2
        guess = list[midValue]

        attempts += 1
        print("#Attempt number {}".format(attempts))

        if guess == item:
            return midValue
        if guess > item:
            higherValue = midValue - 1
        else:
            lowerValue = midValue + 1
        
    return None

        
numbers = []

for i in range(5000):
    numbers.append(i + 1);
    
result = binary_search(numbers, 2500)

if (result == None):
    print("The Number was not found")
else:
    print("Founded on {} index".format(result))