def cleanFile(file):
    '''Strips newline characters and creates a list of the lines, with each line split on ';'
       to seperate the different parts of the logline.'''
    rawLinesList = file.readlines()
    splitLinesList = []
    for line in rawLinesList:
        line = line.strip()
        splitLine = line.split(';')
        splitLinesList.append(splitLine)
    
    return splitLinesList

def dictCounter(totalDict, key, value):
    if value in totalDict[key]:
        totalDict[key][value] += 1
    else:
        totalDict[key][value] = 1

def entryCounter(fileList):
    entryDict = {'frameNum': {}, 'frameTime': {}, 'ipSrc': {}, 'srcPort': {}, 'ipDst': {}, 'dstPort': {}, 'ipProto': {}, 'ipLen': {}, 'proto': {}, 'info': {}}

    for item in fileList:
        for pos, value in enumerate(item):
            # Item length sould be 10 so 0 - 9
            if pos == 0:
                dictCounter(entryDict, 'frameNum', value)
            elif pos == 1:
                dictCounter(entryDict, 'frameTime', value)
            elif pos == 2:
                dictCounter(entryDict, 'ipSrc', value)
            elif pos == 3:
                dictCounter(entryDict, 'srcPort', value)
            elif pos == 4:
                dictCounter(entryDict, 'ipDst', value)
            elif pos == 5:
                dictCounter(entryDict, 'dstPort', value)
            elif pos == 6:
                dictCounter(entryDict, 'ipProto', value)
            elif pos == 7:
                dictCounter(entryDict, 'ipLen', value)
            elif pos == 8:
                dictCounter(entryDict, 'proto', value)
            elif pos == 9:
                dictCounter(entryDict, 'info', value)
            else:
                print('----------SOMETHING WENT WRONG----------')

    return entryDict

# Main
def main():
    fileName = './blue-midterm-log.txt'
    with open(fileName, 'r') as file:
        fileList = cleanFile(file)
    
    countsDict = entryCounter(fileList)

# Dunder check
if __name__ == "__main__":
    main()