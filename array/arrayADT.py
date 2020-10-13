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
        
