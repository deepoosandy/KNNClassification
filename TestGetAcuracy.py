from GeAcurecy import getAcuracy
testSet=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
predictions=['a','a','a']
accuracy=getAcuracy(testSet,predictions)
print(accuracy)