# ===================== HOMEWORK-2A ==============================
# ================================================================


# ===================== Task-1 ===================================
# ================================================================

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if type(d) == int:
            self._coords = [0]*d
        else:
            self._coords = d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]
        
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other # rely on existing eq definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1: -1] + ">" # adapt list representation

# ============================ Task-2 ============================================
# ================================================================================
# Implement the __sub__ method for the Vector class so that the expression u-v returns 
# a new vector instance representing the difference between two vectors.        
        
    def __sub__(self, other):
        """Return a new substacted vector of u-v."""
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

# =========================== Task-3 =================================================================
# ====================================================================================================
# : Implement the __neg__ method for the Vector class so that the expression -v returns 
# a new vector instance whose coordinates are all the negated values of the respective coordinates of v.
  
    def __neg__(self):
        """Return a new vector that has negative values of original vector."""
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)): # implementing the netagive values to new vector
            result[j]  = -self[j]
        return result
        
# =========================== Task-4 =================================================================
# ====================================================================================================
# The Vector implementation in Section 2.3.3 supports a syntax such as v = u + [5, 3, 10, -2, 1], in which 
# the sum of a vector and list returns a new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is illegal. 
# Explain how the Vector class definition can be revised so that this syntax generates a new vector.

# Solution:
# The problem is if we used "+" operator after a list, it directly try to use __add__ method of list class.
# However we just want to use "+" operator of what we have created in Vector class. Therefore, an __radd__ method
# will solve this problem.

    def __radd__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result


# =========================== Task-5 =================================================================
# ====================================================================================================
# Implement the __mul__ method for the Vector class so that the expression v * 3 returns a new vector
# with coordinates that are 3 times the respective coordinates of v.

    def __mul__(self, other):
        if type(other) == int:
            """Return a new vector that is multiple of original vector."""
            for j in range(len(self)):  # multiplying the values to new vector
                self[j] = self[j] * other
            return self
        else:
            """Return the scalar multiplication of 2 vectors."""
            dotProduct = 0
            for i in range(len(self)):
                dotProduct = dotProduct + self[i] * other[i]
            return dotProduct
        
        
# =========================== Task-6 =================================================================
# ====================================================================================================
# Implement the __rmul__ method, to provide additional support for syntax 3 * v.

    def __rmul__(self, other):
        """Return a new vector that is multiple of original vector."""
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):  # multiplying the values to new vector
            result[j] = self[j] * other
        return result


# =========================== Task-7 =================================================================
# ====================================================================================================
# Enhance the __mul__ method for the Vector class so that the expression u * v returns a scalar that
# represents the dot product of the vectors.

# The solution is revised at __mul__ method.        
        
  
# =========================== Task-8 =================================================================
# ====================================================================================================  
# Modify the constructor so that if a single integer is sent, it produces a vector of that dimension with all
# zeros (e.g., Vector(3) should produce <0,0,0> vector), but if a sequence of numbers is provided, it produces a
# vector with coordinates based on that sequence (e.g.,Vector([1,2,3]) should produce <1,2,3> vector).

# The solution is revised at __init__ method.
