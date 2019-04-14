# calling any other file method to other file first key word from then filename then import key
# word then name of the method
from splitdataForKNN import loadDataSet

filename ='D:\\Machine Learing\\iris-species\\Iris.csv'
trainSet=[]
testSet=[]
loadDataSet(filename,0.66,trainSet,testSet)
# print(trainSet)
print('Train: '+repr(len(trainSet)))
print('Test: '+repr(len(testSet)))