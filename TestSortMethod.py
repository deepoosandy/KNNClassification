import operator
List=[([2, 2, 2, 'a'], 1.4142135623730951), ([4, 4, 4, 'b'], 1.4142135623730951), ([3, 3, 3, 'c'], 0.0)]
List.sort(key=operator.itemgetter(1))
print(List)