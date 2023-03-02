import copy
import random

height = 14
width = 10

IPieceBoards = []
# create all possible I piece boards
# vertical I piece
for i in range(width):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(4):
        pieceBoard[j][i] = 1
    IPieceBoards.append(pieceBoard)
# horizontal I piece
for i in range(width - 3):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(4):
        pieceBoard[0][i + j] = 1
    IPieceBoards.append(pieceBoard)

JPieceBoards = []
# create all possible J piece boards
# vertical J piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(3):
        pieceBoard[j][i+1] = 1
    pieceBoard[2][i] = 1
    JPieceBoards.append(pieceBoard)
# other vertical J piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(3):
        pieceBoard[j][i] = 1
    pieceBoard[0][i + 1] = 1
    JPieceBoards.append(pieceBoard)
# horizontal J piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[0][i+1] = 1
    pieceBoard[0][i+2] = 1
    pieceBoard[1][i+2] = 1
    JPieceBoards.append(pieceBoard)
# other horizontal J piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i+2] = 1
    pieceBoard[0][i] = 1
    JPieceBoards.append(pieceBoard)

LPieceBoards = []
# create all possible L piece boards
# vertical L piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(3):
        pieceBoard[j][i] = 1
    pieceBoard[2][i + 1] = 1
    LPieceBoards.append(pieceBoard)
# other vertical L piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    for j in range(3):
        pieceBoard[j][i+1] = 1
    pieceBoard[0][i] = 1
    LPieceBoards.append(pieceBoard)
# horizontal L piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[0][i+1] = 1
    pieceBoard[0][i+2] = 1
    pieceBoard[1][i] = 1
    LPieceBoards.append(pieceBoard)
# other horizontal L piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i+2] = 1
    pieceBoard[0][i+2] = 1
    LPieceBoards.append(pieceBoard)

OPieceBoards = []
# create all possible O piece boards
for i in range(width - 1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[0][i+1] = 1
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    OPieceBoards.append(pieceBoard)

SPieceBoards = []
# create all possible S piece boards
# vertical S piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[2][i+1] = 1
    SPieceBoards.append(pieceBoard)
# horizontal S piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i+1] = 1
    pieceBoard[0][i+2] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i] = 1
    SPieceBoards.append(pieceBoard)

ZPieceBoards = []
# create all possible Z piece boards
# vertical Z piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i+1] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i] = 1
    pieceBoard[2][i] = 1
    ZPieceBoards.append(pieceBoard)
# horizontal Z piece
for i in range(width - 2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[0][i+1] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i+2] = 1
    ZPieceBoards.append(pieceBoard)

TPieceBoards = []
# create all possible T piece boards
# point up T piece
for i in range(width-2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i+1] = 1
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i+2] = 1
    TPieceBoards.append(pieceBoard)
# point down T piece
for i in range(width-2):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[1][i+1] = 1
    pieceBoard[0][i] = 1
    pieceBoard[0][i+1] = 1
    pieceBoard[0][i+2] = 1
    TPieceBoards.append(pieceBoard)
# point left T piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i+1] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[1][i] = 1
    pieceBoard[2][i+1] = 1
    TPieceBoards.append(pieceBoard)
# point right T piece
for i in range(width-1):
    pieceBoard = [[0 for i in range(width)] for j in range(height)]
    pieceBoard[0][i] = 1
    pieceBoard[1][i] = 1
    pieceBoard[1][i+1] = 1
    pieceBoard[2][i] = 1
    TPieceBoards.append(pieceBoard)

# _________________________________________________________________
# start of important code
# _________________________________________________________________

class Tetris:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = tuple([tuple([0 for i in range(self.width)]) for j in range(self.height)])
        self.score = 0

    def __hash__(self):
        return hash(self.board)
    
    def __eq__(self, other):
        if self.board == other.board:
            self.score = max(self.score, other.score)
            other.score = max(self.score, other.score)
            return True
        # check for mirror image
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != other.board[i][self.width - j - 1]:
                    return False
        self.score = max(self.score, other.score)
        other.score = max(self.score, other.score)
        return True

    def updateBoard(self):
        totalCleared = 0
        for i in range(self.height):
            if self.isRowFull(i):
                self.clearRow(i)
                totalCleared += 1
        # arbitrary scoring system
        if totalCleared == 1:
            self.score += 40
        elif totalCleared == 2:
            self.score += 100
        elif totalCleared == 3:
            self.score += 300
        elif totalCleared == 4:
            self.score += 1200

    # hole checker for heuristic purposes
    def hasHole(self, row, cell):
        for i in range(row, self.height):
            if self.board[i][cell] == 1 and self.board[row][cell] == 0:
                return True
        return False
    
    # Ethan's silly hole heuristic
    # 1
    # 0
    # is a 1 point hole
    # 1
    # 0 
    # 0
    # is a 2 point hole
    # 1
    # 1
    # 0
    # is also a 2 point hole
    def holeHeuristicScore(self):
        # check each column
        score = 0
        for i in range(self.width):
            # count how many 0s are at the top of the column and 
            # how many 1s are at the bottom of the column
            # everything else is part of a hole
            numZeros = 0
            for j in range(self.height):
                if self.board[j][i] == 0:
                    numZeros += 1
                else:
                    break
            numOnes = 0
            for j in range(self.height-1, -1, -1):
                if self.board[j][i] == 1:
                    numOnes += 1
                else:
                    break
            score += height - (numZeros + numOnes)
        return score
                
                

    #used to check to see if a row should be cleared
    def isRowFull(self, row):
        for i in range(self.width):
            if self.board[row][i] == 0:
                return False
        return True


    def clearRow(self, row):
        listBoard = [list(i) for i in self.board]
        for i in range(row, 0, -1):
            for j in range(self.width):
                listBoard[i][j] = listBoard[i-1][j]
        self.board = tuple(tuple(i) for i in listBoard)

    def printBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.board[i][j], end=' ')
            print()
        print('-----------------')
    
    def slam(self, pieceBoard): # piece is a 20 x 10 board with just the piece that is falling
        # we want to make this piece slam as far down as possible

        # find the columns in pieceBoard that are not empty and find their furthest down position that is non empty
        # then we want to find the min distance between those columns and non empty columns on the board
        # then we want to move the piece down by that distance

        # find the columns in pieceBoard that are not empty

        lowestPositions = [-1 for i in range(self.width)]
        piecePositions = []
        for i in range(self.height):
            for j in range(self.width):
                if pieceBoard[i][j] != 0:
                    lowestPositions[j] = i
                    piecePositions.append((i, j))
        
        highestPositions = [self.height for i in range(self.width)]
        for i in range(self.height - 1, -1, -1):
            for j in range(self.width):
                if self.board[i][j] != 0:
                    highestPositions[j] = i
        
        minDistance = self.height
        for i in range(self.width):
            if lowestPositions[i] != -1:
                minDistance = min(minDistance, highestPositions[i] - lowestPositions[i])
        
        # create a list version of the board
        # move the piece down by minDistance
        # then update the board
        listBoard = [list(row) for row in self.board]

        for position in piecePositions:
            listBoard[position[0] + minDistance - 1][position[1]] = pieceBoard[position[0]][position[1]]
        self.board = tuple(tuple(row) for row in listBoard)

    def findSuccessors (self, piece):
        # find successors also uses heuristic to choose which successor to return
        newBoards = set()
        pieceBoards = []
        if piece == 'I':
            pieceBoards = IPieceBoards
        elif piece == 'J':
            pieceBoards = JPieceBoards
        elif piece == 'L':
            pieceBoards = LPieceBoards
        elif piece == 'O':
            pieceBoards = OPieceBoards
        elif piece == 'S':
            pieceBoards = SPieceBoards
        elif piece == 'Z':
            pieceBoards = ZPieceBoards
        elif piece == 'T':
            pieceBoards = TPieceBoards
        else:
            print('invalid piece')
        
        for pieceBoard in pieceBoards:
            newBoard = self.copy()
            if not newBoard.isGameOver(pieceBoard):
                newBoard.slam(pieceBoard)
                newBoard.updateBoard()
                r = random.random()
                if r < 0.25:
                    holescore = newBoard.holeHeuristicScore()
                    r = random.random()
                    if holescore == 0:
                        newBoards.add(newBoard)
                    elif r < 1/holescore:
                        newBoards.add(newBoard)
        return newBoards
        
    def isGoodSetup(self):
        # return False if there is a 1 above a 0
        for i in range(self.height - 1):
            for j in range(self.width):
                if self.board[i][j] == 1 and self.board[i+1][j] == 0:
                    return False
        return True

    def isGameOver(self, pieceBoard):
        # if there is any overlap in the board and pieceboard game is over
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != 0 and pieceBoard[i][j] != 0:
                    return True
        return False
    
    def copy(self):
        t = Tetris(self.height, self.width)
        t.board = copy.deepcopy(self.board)
        t.score = self.score
        return t
    
def generateRandomPieceOrder(numPieces):
    pieces = ['I', 'J', 'L', 'O', 'S', 'Z', 'T']
    # sample numPieces pieces from pieces
    return random.choices(pieces, k=numPieces)

def generateRandomBoard(height, width, numPieces):
    pieceOrder = generateRandomPieceOrder(numPieces)
    t = Tetris(height, width)
    for piece in pieceOrder:
        print("start")
        successors = t.findSuccessors(piece)
        if len(successors) == 0:
            break
        t = random.choice(list(successors))
    t.printBoard()
    return t.board

def simulate(numPieces, initialState, height, width):
    pieces = ['I', 'J', 'L', 'O', 'S', 'Z', 'T']
    pieceOrder = generateRandomPieceOrder(numPieces)
    t = Tetris(height, width)
    t.board = initialState
    pieceScores = {}
    for piece in pieces: # need to think about how to record a score if a game ends early
        successors = t.findSuccessors(piece)
        if len(successors) == 0:
            pieceScores[piece] = 0
        for newPiece in pieceOrder:
            # print("calculating score for new piece: " + newPiece + "")
            newSuccessors = set()
            for successor in successors:
                newSuccessors = newSuccessors.union(successor.findSuccessors(newPiece))
            if len(newSuccessors) == 0:
                break
            successors = newSuccessors
        maxScore = 0
        for successor in successors:
            maxScore = max(maxScore, successor.score)
        pieceScores[piece] = maxScore
        # print("done calculating score for piece: " + piece + "")
    return pieceScores
for _ in range(20):
    state = generateRandomBoard(14, 10, 5)
    total = simulate(6, tuple([tuple([0 for i in range(10)]) for j in range(14)]), 14, 10)
    for i in range(20):
        result = simulate(6, tuple([tuple([0 for i in range(10)]) for j in range(14)]), 14, 10)
        for piece in result:
            total[piece] += result[piece]
    for piece in total:
        total[piece] /= 21
    print(total)
#test to make sure slamming works
# t = Tetris(height, width)
# pieceBoard = [[0 for i in range(10)] for j in range(24)]
# pieceBoard[0][0] = 1
# pieceBoard[0][1] = 1
# pieceBoard[0][2] = 1
# pieceBoard[0][3] = 1
# t.slam(pieceBoard)
# t.printBoard()
# pieceBoard [0][0] = 0
# pieceBoard [1][1] = 1
# t.slam(pieceBoard)
# t.printBoard()
# pieceBoard = [[0 for i in range(10)] for j in range(24)]
# pieceBoard[0][0] = 1
# pieceBoard[1][0] = 1
# pieceBoard[2][0] = 1
# pieceBoard[3][0] = 1
# t.slam(pieceBoard)
# t.printBoard()

# t = Tetris(height, width)
# newIBoards = t.findSuccessors('S')
# for board in newIBoards:
#     board.printBoard()