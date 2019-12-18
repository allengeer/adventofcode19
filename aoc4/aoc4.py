import collections
passwordList = range(197487,673251)
increasingPasswords = filter(lambda x: list(str(x)) == sorted(list(str(x))), passwordList)
doubleDigitPasswords = filter(lambda x: len(set(list(str(x)))) != len(str(x)), increasingPasswords)
largerGroupFilter = filter(lambda x: 2 in collections.Counter(list(str(x))).values(), doubleDigitPasswords)
print len(increasingPasswords), len(doubleDigitPasswords), len(largerGroupFilter)