from GetNeighbour import getNeighbour
trainingSet=[[2,2,2,'a'],[4,4,4,'b']]
testSet=[5,5,5]
k=1
neighbours=getNeighbour(trainingSet,testSet,k)
print(neighbours)