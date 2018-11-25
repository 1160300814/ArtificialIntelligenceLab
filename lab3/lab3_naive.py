# global value
N = 0
nameList = []
file1 = 'burglarnetwork.txt'
file2 = 'burglarqueries.txt'

# seq < 2^n
def getChartIndex(seq, uppernodes, n):
    index = seq
    k = 0
    for i in range(n):
        if n - 1 - i in uppernodes:
            k += 1
        else:
            index = (index >> (k + 1) << k) + index % (1 << k)
    return index

def getIndexByNameVal(nameVal):
    global nameList
    nameVal = nameVal.strip()
    tempList = nameVal.split('=')
    name = tempList[0]
    val = tempList[1]
    i = nameList.index(name)
    if val == 'true':
        val = True
    elif val == 'false':
        val = False
    else:
        print 'Input Error' + str(val)
    return i, val

def parseExpression(express):
    print express
    global N
    tempList = express.split('|')
    exp1 = tempList[0].strip()
    tempList = tempList[1].split(',')
    flagbitsCon = 0
    flagbitsAll = 0
    valuebits = 0
    for ele in tempList:
        i, val = getIndexByNameVal(ele)
        flagbitsCon |= 1 << (N - 1 - i )
        if val:
            valuebits |= 1 << (N - 1 - i )
    flagbitsAll = flagbitsCon | 1 << (N - 1 - nameList.index(exp1))
    return flagbitsAll, flagbitsCon, valuebits

def getExpression(inputString):
    inputString = inputString.strip('P(')
    tempList_1 = inputString.split('P(')
    tempList_2 = [ele.strip().strip(')') for ele in tempList_1]
    # for ele in tempList_1:
    #     tempList_2.append(ele.replace(')', ''))
    return tempList_2

def main():
    global N, nameList, file1, file2
    f = open(file1, 'r') 
    N = eval(f.readline()) 
    totalChart = [0] * (1 << N)
    totalChart[0] = 1
    f.readline()  
    nameList = f.readline().split()  
    roots = [[] for i in range(N)]  
    f.readline()  
    for i in range(N):  
        str_in = f.readline()  
        row = [int(n) for n in str_in.split()]  
        for j in range(N):  
            if row[j] == 1:  
                roots[j].append(i)  

    n = 0
    for i in range(N):
        f.readline()
        rowLen = 1 << len(roots[i])
        chart = [[] for i in range(rowLen)]

        for j in range(rowLen):
            str_in = f.readline()
            chart[j] = [float(x) for x in str_in.split()]
        # print '---CHART---'
        # for i in range(len(chart)):
        #     print chart[i]
        # print '|--CHART--|'
        tempChart = [x for x in totalChart]
        for i in range(1 << (n+1)):
            totalChart[i] = tempChart[i // 2] * chart[getChartIndex(i // 2, roots[n], n)][1 - i % 2]
        n += 1
        # print '---totalchart---'
        # print totalChart
        # print '|--totalchart--|'
    f.close()
    sum = 0
    # for i in range(1 << N):
    #     sum += totalChart[i]
    # print 'sum=' + str(sum)

    f = open(file2, 'r')
    inputString = f.read()
    expressionList = getExpression(inputString)
    for entry in expressionList:
        flagbitsAll, flagbitsCon, valuebits = parseExpression(entry)
        pCon, pT, pF= 0, 0, 0
        for i in range(1 << N):
            if i & flagbitsCon == valuebits:
                pCon += totalChart[i]
                if i & flagbitsCon == i & flagbitsAll:
                    pF += totalChart[i]
                else:
                    pT += totalChart[i]
        print format(pF/pCon, '.3f'), format(pT/pCon, '.3f')
    f.close()

if __name__ == '__main__':
    main()