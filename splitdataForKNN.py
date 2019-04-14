import csv
import random
def loadDataSet(fileName, splitRatio, traingingSet=[],testSet=[]):
    with open(fileName,'r') as csvfile:
        lines=csv.reader(csvfile)
        dataset=list(lines)
        # print(dataset)
        for x in range(len(dataset)):
            for y in range(5):
                # if x < len(dataset)-1:
                #     x=x+1
                dataset[x][y]=float(dataset[x][y])
                
            if random.random() < splitRatio :
                  traingingSet.append(dataset[x])  
                #   print("Train: "+repr(dataset[x]))
            else:
                    testSet.append(dataset[x])
                    # print("Test: "+repr(dataset[x]))