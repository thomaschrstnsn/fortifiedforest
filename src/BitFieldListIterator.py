class BitFieldListIterator:
    """Bitfield implementation which can be used as a iterator.
    It will iterate over all the possible permutations returning a list of the 1-bits,
    e.g. 0 yields [], 1 yields [1], 2 yields [2], 3 yields [1 2], etc.
"""
    def __init__(self, numBits, startValue = 0, stepsize = 1, zeroIndexed = False):
        self.numBits = numBits
        self.max = 2 ** numBits
        self.current = startValue
        self.stepsize = stepsize
        self.zeroIndexed = zeroIndexed
    
    def __iter__(self):
        return self

    def _currentToList(self):
        result = []
        for bit in range(0, self.numBits):
            mask = 1 << bit
            if (self.current & mask) != 0:
                if self.zeroIndexed:
                    result.append(bit)
                else:
                    result.append(bit + 1)
        return result

    def next(self):
        if self.current >= self.max:
            raise StopIteration
        result = self._currentToList()
        self.current = self.current + self.stepsize
        return result
