def add(numbers):
    """
    Accept a string of delimited values and add them together.
    """

    #Check if the string contains values. If empty, return 0 else return sum.
    if len(numbers) > 0:

        stringList = numbers.split(',')
        
        mapObject = map(int, stringList)

        integerList = list(mapObject)

        return sum(integerList)

    else:
        return 0

val = add('1,2,3')
print(val)
