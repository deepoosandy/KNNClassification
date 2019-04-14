import operator
def getResponse(neighbours):
    classsVotes={}
    # print(neighbours)
    for x in range (len(neighbours)):
        # print(neighbours[x][-1])
        response=neighbours[x][-1]
        if response in classsVotes:
            classsVotes[response]+=1
        else:
            classsVotes[response]=1
    # print(classsVotes)
    sortedVotes=sorted(classsVotes.items(),key=operator.itemgetter(1),reverse=True)
    # print(sortedVotes)
    return sortedVotes[0][0]