def check_gradient(array):
    pairs = list(zip(array[0:-1], array[1:]))

    filtered_pairs = list(filter(lambda tup: tup[0] < tup[1], pairs))
    print(len(filtered_pairs))


inputFile = open("input")

intArray = list(map(lambda x: int(x), inputFile))

# Part one solution...
check_gradient(intArray)

# part two
sumWindows = list(map(sum, zip(intArray[0:-2], intArray[1:-1], intArray[2:])))
check_gradient(sumWindows)
