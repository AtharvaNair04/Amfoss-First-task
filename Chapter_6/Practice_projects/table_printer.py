def printTable(tableData):
    colWidths=[0]*len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            colWidths[i]=max(colWidths[i],len(tableData[i][j]))
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(colWidths[j]+1),end=' ')
        print()
tableData=[['apples','oranges','cherries','banana'],
             ['Alice','Bob','Carol','David'],
             ['dogs','cats','moose','goose']]
printTable(tableData)
