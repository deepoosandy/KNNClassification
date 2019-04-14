from splitdataForKNN import loadDataSet
from GetNeighbour import getNeighbour
from GetResponse import getResponse
from GeAcurecy import getAcuracy

def main():
    filename = 'D:\\Machine Learing\\iris-species\\Iris.csv'
    trainSet=[]
    testSet=[]
    split=0.67
    loadDataSet(filename,split,trainSet,testSet)
    # print(trainSet[1])
    print('Train: '+repr(len(trainSet)))
    print('Test: '+repr(len(testSet)))
    prediction=[]
    k=3
    for x in range(len(testSet)):
        # print(testSet[x])
        neighbours=getNeighbour(trainSet,testSet[x],k)
        result=getResponse(neighbours)
        prediction.append(result)
        # print('> predicted = '+repr(result) +" , actual= "+repr(testSet[x][-1]))
    
    # print(prediction)
    accuracy=getAcuracy(testSet,prediction)
    print(accuracy)
main()






