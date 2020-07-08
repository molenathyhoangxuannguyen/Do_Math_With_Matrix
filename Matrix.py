def dot( vec1, vec2 ):
    """
    Creating the dot product
    """
    mul = [i * j for i, j in zip(vec1, vec2)] # i is self.row, j = other.col, multiply each thing in vec
    add = sum(mul)
    return add

class Matrix():

    def __init__( self, matrix ):
        self.matrix = matrix
        self.row = self.get_row(matrix)
        self.col = self.get_col(matrix)

    def get_row( self , i):
        '''
        Finding how many rows are in the matrix
        '''
        rows = 0
        for row in i:
            rows += 1
            try:
                for j in row:
                    pass
            except:
                return 1

        return rows


    def get_col( self , j):
        '''
        finding how many colums in the Matrix
        '''
        cols = 0
        for row in j:
            try:
                for col in row:
                    cols +=1
                return cols

            except:
                cols +=1

        return cols


    def add( self, other ):
        '''
        finding the sum of the matrix the long way
        '''
        if (self.row != other.row) or (self.col != other.col):
            print("Can not add these two matrix")
            return
        matrix = self.matrix
        add = []
        temp = []
        r = 0
        c = 0
        try:
            for i in (matrix):
                temp = []
                for j in i:
                    temp.append(self.matrix[r][c] + other.matrix[r][c])

                    c += 1
                add.append(temp)
                r += 1
                c = 0

        except:
            for i in range(len(matrix)):
                add.append(self.matrix[i] + other.matrix[i])
        return add


    def sub( self, other ):
        '''
        Finding the subtracted the long way
        '''
        if (self.row != other.row) or (self.col != other.col):
            print("Can not subtract these two matrix")
            return
        matrix = self.matrix
        sub = []
        temp = []
        r = 0
        c = 0
        try:
            for i in (matrix):
                temp = []
                for j in i:
                    temp.append(self.matrix[r][c] - other.matrix[r][c])

                    c += 1
                sub.append(temp)
                r += 1
                c = 0

        except:
            for i in range(len(matrix)):
                sub.append(self.matrix[i] - other.matrix[i])
        return sub


    def mult( self, other ):
        '''
        multiplying using the dot product and through the scalar multiplacation
        '''
        multiply = []
        try:
            isInt = other + 1
            for row in self.matrix:
                mul = [other * i for i in row] # i is self.row, j = other.col, multiply each thing in vec
                multiply.append(mul)
            return multiply

        except:
            if (self.row == other.col):
                for i in range(other.row):
                    for j in range(other.col):
                        selfVector = []
                        otherVector = []
                        newRow =[]
                        for r in range(self.col):
                            selfVector.append(other.matrix[i][r])
                            otherVector.append(self.matrix[r][j])
                            newRow.append(dot(selfVector, otherVector))
                    multiply.append(newRow)
                return multiply

            elif (self.col == other.row):
                for i in range(self.row):
                    for j in range(self.col):
                        selfVector = []
                        otherVector = []
                        newRow =[]
                        for r in range(other.col):
                            selfVector.append(self.matrix[i][r])
                            otherVector.append(other.matrix[r][j])
                            newRow.append(dot(selfVector, otherVector))
                    multiply.append(newRow)
                return multiply


            else:
                print('Can not multiply these matrix')



    ## TODO
    ## Return a Matrix that is the transpose of self.
    def transpose( self ):
        '''
        flipping the row and colum of the Matrix
        '''
        transpose = []
        newRow = []
        for r in range(self.col):
            newRow = []
            for i in range(self.row):
                newRow.append(0)
            transpose.append(newRow)

        for r in range(self.row):
            for c in range(self.col):
                transpose[c][r] = self.matrix[r][c]
        return transpose


def main():
    m1 = Matrix([[1,2,3],
                [4,5,6]])
    m2 = Matrix([[4,5,6],
                [6,5,4]])
    print('m1 = ')
    for i in m1.matrix:
        print(i)
    print('m2 = ')
    for i in m2.matrix:
        print(i)
    print('\n')
    print("m1 + m2 = ")
    m3 = m1.add(m2)
    for i in m3:
        print(i)
    print("\n")

    print('m2 - m1 = ')
    m3 = m2.sub(m1)
    for i in m3:
        print(i)
    print('\n')

    print('m1 transpose = ')
    m3 = m1.transpose()
    for i in m3:
        print(i)
    print("\n")

    m4 = Matrix([[3, 2, 1],
                [4,3, 2],
                [5,4, 5]])
    print('m4 = ')
    for i in m4.matrix:
        print(i)
    print('\n')
    print('m1 x m4 = ')
    m3 = m1.mult(m4)
    for i in m3:
        print(i)
    print('\n')

    m3 = m1.mult(3)
    print('m1 x 3 = ')
    for i in m3:
        print(i)


main()
