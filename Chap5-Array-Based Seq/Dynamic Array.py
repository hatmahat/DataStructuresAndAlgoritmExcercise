import ctypes                    # Provides low-level arryas

class DynamicArray:
    """A dynamic array class akin to splified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._n = 0                                 # count actual elements
        self._capacity = 1                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level aray

    def __len__(self):
        """Return number of elements stored in the arrya."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                           # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:               # not enough room
            self._resize(2 * self._capacity)        # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                           # nonpublic utitity
        """Rsize internal array to capacity c."""
        B = self._make_array(c)                     # new (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B                                 # use the bigger array

    def _make_array(self, c):                       # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)( )            # see ctypes documentation