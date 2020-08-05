import re

def isEmpty(string):
    return len(string) > 0

def getDelimiter(string):
    if string.startswith('//'):
        delimiters = re.findall(r'(?<=\/\/)(.*?)\n', string)

        return ('|'.join(delimiters), string[string.index('\n') + 1:])
    else:
        return ('\n|,', string)

def add(numbers):
    """
    Accept a string of delimited values and add them together.
    """

    values = getDelimiter(numbers)

    delimiters = values[0]
    numbers = values[1]

    stringList = re.split(delimiters, numbers)

    mapObject = map(int, filter(isEmpty, stringList))

    integerList = list(mapObject)

    return sum(integerList)


