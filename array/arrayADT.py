import ctypes as _ct
from copy import copy as _cp
from copy import deepcopy as _dp
from collections import OrderedDict as _od

class Array:  
    def __init__(self, size):
        assert isinstance(size, int), 'The size of array must be an integer'
        assert size > 0, 'The size must be greater than 0'

        self._size = size
        PyArrayType = _ct.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value


    def __iter__(self):
        return _ArrayIterator(self._elements)

    def __str__(self):
        S = '['
        for i in range(self._size):
            S += (str(self._elements[i]) + ', ')
        S = S[:-2]
        S += ']'
        return S

    def __repr__(self):
        S = '['
        for i in range(self._size):
            S += (str(self._elements[i]) + ', ')
        S = S[:-2]
        S += ']'
        return S

    def __contains__(self, target):
        return self.contains(target)

    def contains(self, target):
        for element in self._elements:
            if element == target:
                return True
        else:
            return False
        
    def count(self, target):
        counter = 0
        for i in range(self._size):
            if target == self._elements[i]:
                counter += 1
        return counter
        
    def copy(self):
        X = Array(len(self))
        for i, j in enumerate(self):
            X[i] = j
        return X
    
    def index(self, value):
        for i, j in enumerate(self):
            if j == value:
                return i
        else:
            return None
        
        
    def __add__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] + val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] + val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    
    def __sub__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] - val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] - val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        
        
    def __mul__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] * val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] * val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        

    def __truediv__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] / val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] / val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')        
    
    def __floordiv__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] // val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] // val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
        
    def __mod__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] % val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] % val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __pow__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ** val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ** val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
    
    def __lshift__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] << val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] << val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __rshift__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >> val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >> val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __and__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] & val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] & val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __or__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] | val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] | val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')

    def __xor__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ^ val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] ^ val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
    
    def __pos__(self):
        return self.copy()
    
    def __neg__(self):
        return -1 * self.copy()
    
    def __iadd__(self, val):
        self = self + val
    
    def __isub__(self, val):
        self = self - val
        
    def __imul__(self, val):
        self = self * val
        
    def __itruediv__(self, val):
        self = self / val
    
    def __ifloordiv__(self, val):
        self = self // val
        
    def __imod__(self, val):
        self = self % val
        
    def __ilshift__(self, val):
        self = self << val
        
    def __irshift__(self, val):
        self = self >> val
        
    def __ipow__(self, val):
        self = self ** val
        
    def __iand__(self, val):
        self = self & val
        
    def __ior__(self, val):
        self = self | val
        
    def __ixor__(self, val):
        self = self ^ val        
    
    def __abs__(self):
        total = Array(len(self))
        for index in range(len(self)):
            total[index] = abs(self[index])
            
        return total
    def __invert__(self):
        total = Array(len(self))
        for index, val in enumerate(self):
            total = ~val
            
        return total
    
    def __lt__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] < val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] < val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __gt__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] > val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] > val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __eq__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] == val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] == val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')

    def __le__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] <= val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] <= val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __ge__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >= val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] >= val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
    def __ne__(self, val):
        if isinstance(val, (int, float)):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] != val
            return total
        elif isinstance(val, (list, tuple, Array)) and len(self) == len(val):
            total = Array(len(self))
            for i in range(len(self)):
                total[i] = self[i] != val[i]
            return total
        else:
            raise TypeError('Operation between invalid types.')
        
class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        self._curNdx = 0
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])
    
    def shape(self):
        return self.numRows(), self.numCols()
    
    def size(self):
        return self.numRows() * self.numCols()

    def clear(self, value):
        for row in self._theRows:
            row.clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        
        row = ndxTuple[0]
        col = ndxTuple[1]

        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

    def __str__(self):
        S = str()
        for row in self._theRows:
            S += (str(row) + "\n")
        return S

    def __repr__(self):
        return str(self)
    

    def returnRow(self, row):
        assert row in range(0, self.numRows()), "Invalid Row"
        return self._theRows [ row ]
    
    def returnCol(self, col):
        assert col in range(0, self.numCols()), "Invalid Column"
        newArray = Array(self.numRows())
        for i in range(self.numRows()):
            row = self._theRows[i]
            newArray[i] = row [col]
        return newArray
    
    def __iter__(self):
        self._curNdx = 0
        return self
    
    def __next__(self):
        row = self._curNdx // self.numCols()
        col = self._curNdx % self.numCols()
        
        if self._curNdx < (self.numCols() * self.numRows()):
            self._curNdx += 1
            iterRow = self._theRows[row]
            return iterRow[col]
        else:
            raise StopIteration
        
    def copy(self):
        copyArray = Array2D(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                copyArray[i, j] = self[i, j]
        return copyArray
    
    def count(self, target):
        count = 0
        for i in range(self.numRows()):
            X = self._theRows[i]
            count += X.count(target)
        
        return count
    
    def index(self, value):
        for xNum, row in enumerate(self._theRows):
            for yNum, val in enumerate(row):
                if val == value:
                    return xNum, yNum
        
        return None, None
    
    def __len__(self):
        return self.numRows()
    
    def __add__(self, val):
        if isinstance(val, (int, float)):
            total = Array2D(self.numRows(), self.numCols())
            for i in range(self.numRows()):
                for j in range(self.numCols()):
                    total[i, j] = self[i, j] + val
            return total
        elif isinstance(val, Array2D) and self.shape() == val.shape():
            total = Array2D(self.numRows(), self.numCols())
            for i in range(self.numRows()):
                for j in range(self.numCols()):
                    total[i, j] = self[i, j] + val[i, j]
            return total


class MultiArray:
        
    def __init__(self, *dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."

        self._dims = dimensions
        size = 1
        for dim in dimensions:
            assert dim > 0, "Dimensions must be > 0."
            size *= dim
        self._elements = Array(size)
        self._factors = Array(len(dimensions))
        self._factors.clear(1)
        self._computeFactors()

    def numDims(self):
        return len(self._dims)

    def length(self, dim):
        assert dim > 0 and dim < len(self._dims), "Dimension component out of range."
        return self._dims[dim - 1]

    def clear(self, value):
        self._elements.clear(value)
    
    def shape(self):
        dims = _cp(self._dims)
        return dims

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."

        index = self._computeIndex(ndxTuple)
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    def _computeIndex(self, idx):
        offset = 0
        for i, j in enumerate(idx):
            if j < 0 and j > self._dims[i]:
                return None
            else:
                offset += self._factors[i] * j
        return offset

    def _computeFactors(self):
        for i in range(1, len(self._factors)):
            self._factors[len(self._factors) -i - 1] = self._factors[len(self._factors)-i] * self._dims[len(self._factors)-i]

class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
