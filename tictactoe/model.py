class ColIndexOutOfBound(Exception):
    pass

class RowIndexOutOfBound(Exception):
    pass

class LineIndexOutOfBound(Exception):
    
    def __init__(self, i):
        self.index = i

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
            raise LineIndexOutOfBound(i)

    def next(self, i):
        if i >= 0 and i < self._length-1:
            return i+1
        elif i is self._length-1:
            return None
        else:
            raise LineIndexOutOfBound(i)

class SquareNav:
    """

    """

    def __init__(self, s):
        self.scale = LineNav(s)
        self.corners = [
            (self.getPrevInRow, self.getPrevInCol),
            (self.getNextInRow, self.getPrevInCol),
            (self.getNextInRow, self.getNextInCol),
            (self.getPrevInRow, self.getNextInCol)
        ]


    def getPrevInRow(self, n):
        try:
            if self.scale.prev(self.getCol(n)) is not None:
                result = n-1
            else:
                result = None
            return result
        except LineIndexOutOfBound as e:
            raise ColIndexOutOfBound

    def getNextInRow(self, n):
        try:
            if self.scale.next(self.getCol(n)) is not None:
                result = n+1
            else:
                result = None
            return result
        except LineIndexOutOfBound as e:
            raise ColIndexOutOfBound

    def getPrevInCol(self, n):
        try:
            if self.scale.prev(self.getRow(n)) is not None:
                result = n-self.scale.len()
            else:
                result = None
            return result
        except LineIndexOutOfBound as e:
            raise RowIndexOutOfBound

    def getNextInCol(self, n):
        try:
            if self.scale.next(self.getRow(n)) is not None:
                result = n+self.scale.len()
            else:
                result = None
            return result
        except LineIndexOutOfBound as e:
            raise RowIndexOutOfBound

    def getToCor(self, corner, n):
        x = self.corners[corner][0](n)
        return self.corners[corner][1](x) if x is not None else None

    def getRow(self, n):
        return int(n/self.scale.len())

    def getCol(self, n):
        return n%self.scale.len()


class Vari:

    def __init__(self, id):
        self.id = id

class Kuchchi:
    
    def __init__(self, vari_id, part):
        self.vari_id = vari_id
        self.part = part

class Kattu:

    def __init__(self, kuchchigal, user):
        self.user = user
        self.kuchchigal = kuchchigal

class Kaaigal:

    def __init__(self, user, varigal):
        self.user = user
        self.varigal = varigal

    def maththi(self):
        self.varigal.chear(Kattu(
                [Kuchchi(i, 0) for i in range(0, 4)],
                self.user
            ))

    def monai0(self):
        self.varigal.chear(Kattu(
                [
                    Kuchchi(0, 1),
                    Kuchchi(4, 1),
                    Kuchchi(6, 1)
                ],
                self.user
            ))
        
    def monai1(self):
        self.varigal.chear(Kattu(
                [
                    Kuchchi(2, 1),
                    Kuchchi(4, -1),
                    Kuchchi(7, 1)
                ],
                self.user
            ))
        
    def monai2(self):
        self.varigal.chear(Kattu(
                [
                    Kuchchi(0, -1),
                    Kuchchi(5, -1),
                    Kuchchi(7, -1)
                ],
                self.user
            ))
        
    def monai3(self):
        self.varigal.chear(Kattu(
                [
                    Kuchchi(2, -1),
                    Kuchchi(5, 1),
                    Kuchchi(6, -1)
                ],
                self.user
            ))

class Varigal:
    pass

class Palagai:

    def __init__(self):
        self.varigal = Varigal([Vari(i) for i in range(0, 8)])
        self.kaaigal0 = Kaaigal(0, self.varigal)
        self.kaaigal1 = Kaaigal(1, self.varigal)

