def getAcuracy(testSet,predictions):
    correct=0
#     print(predictions)
    for x in range(len(testSet)):
        # print((testSet[x][-1]) ==(predictions[x]))
        # print(predictions[x])
        # if testSet[x][-1] is predictions[x] :
        # previous one was above line that has change to below line
        if (testSet[x][-1]) ==(predictions[x]):
                # print("reached here")
                correct=correct+1
        # print(correct)
    return (correct/float(len(testSet)))*100
    