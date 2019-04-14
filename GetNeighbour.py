import operator
from EclideanDistance import eudlideanFuction

def getNeighbour(trainingSet, testInstance, k):
    distances=[]
    
    length=len(testInstance)-1
    for x in range(len(trainingSet)):
      dist=eudlideanFuction(trainingSet[x],testInstance,length)
      distances.append((trainingSet[x],dist))
      
   
    distances.sort(key=operator.itemgetter(1))
    # print(distances)
    neighbours=[]
    for x in range(k):
     neighbours.append(distances[x][0])
    
    return neighbours
