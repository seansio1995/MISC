def maxSquare(matrix1):
        # write your code here
        #题都他妈读错了，题的意思是square里面全是1，求这样最大的square的面积
        r=len(matrix1)
        c=len(matrix1[0])
        state=[[0 for x in range(c)] for y in range(r)]

        for i in range(r):
            for j in range(c):
                if matrix1[i][j]==1:
                    state[i][j]=1
        maxLength=1
        for i in range(1,r):
            for j in range(1,c):
                if state[i][j]==1:
                    state[i][j]=1+min(min(state[i][j-1],state[i-1][j]),state[i-1][j-1])
                    if maxLength < state[i][j]:
                        maxLength=state[i][j]
        # print(type(matrix1[0][0])
        # print(state)
        return maxLength*maxLength


matrix1=[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
print(maxSquare(matrix1))
