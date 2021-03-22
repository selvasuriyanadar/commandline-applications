class RowDoesNotExist(Exception):
    pass

class RowIndexOutOfBound(Exception):
    pass

class LineIndexOutOfBound(Exception):
    pass

class LineNav:
    """
    fields:
        length is the length of the line within which navigation occurs
        the positions of the line are given by integers arraged in ascending
    order starting from zero upto the number just before the length of the
    line.
        the first position of the line has no previous position.
        the last position of the line has no next position.

    methods:
        prev gets the previous position in the line to the input
    position if exists otherwise None. throws an exception if the position does
    not exist in the line.
        next gets the next position in the line to the input
    position if exists otherwise None. throws an exception if the position does
    not exist in the line.

    input:
        i which indicates a position in line
    """

    def __init__(self, length):
        self._length = length

    def len(self):
        return self._length
    
    def prev(self, i):
        if i > 0 and i < self._length:
            return i-1
        elif i is 0:
            return None
        else:
            raise LineIndexOutOfBound

    def next(self, i):
        if i >= 0 and i < self._length-1:
            return i+1
        elif i is self._length:
            return None
        else:
            raise LineIndexOutOfBound


class tictactoe:
    """
    fields:
       the board contains 9 boxes.
       the board is a dict with integer keys and integer values.
       the keys of the board dict represent box number and the values represent
    the mark (none, circle, cross) put on the box.
       the none mark is represented by zero the marks cross and circle are
    represented by 1 and 2 respectively and these are constants.
       a box with none mark can only be marked with any other mark only once.
       the twins is a dict with keys as the pairs of boxes that has a chance for
    getting a win and the box which may form the win trio with the pair as the
    value.
       
    """
    
    def __init__(self):
        self._board = {n:0 for n in range(1, 10)}
        self._cross = 1
        self._circle = 2
        self.scale = LineNav(3)
        self._twins = {}

    def _markBox(self, n, mark):
        if not self._board[n]:
            self._board[n] = mark

    def crossBox(self, n):
        self._markBox(n, self._cross)

    def circleBox(self, n):
        self._markBox(n, self._circle)

    def findTwin(self, n):
        
    def exploreTwins(self, n):

        def splitRows(r):
            boxes_behind = r*self.scale.len()
            return self._board[boxes_behind:boxes_behind+self.scale.len()]

        def getPrevInRow(rn):
            try:
                return self.scale.prev(rn)
            except LineIndexOutOfBound as e:
                raise RowIndexOutOfBound

        def getAheadInRow(rn):
            try:
                return self.scale.next(rn)
            except LineIndexOutOfBound as e:
                raise RowIndexOutOfBound

        def getUpInCol(r, rn):
            if not self.scale.prev(r):
                

        def getDownInCol(r, rn):
            pass

        def getRow(n):
            return n/row_box_count

        def exploreHorizontal(n):
            pass

