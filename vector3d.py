import math

class Vector3D:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def norm(self):
        return math.sqrt(self.x^2 + self.y^2 + self.z ^2)

    def __add__(self, other):
        return Vecotr3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vecotr3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vecotr3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def getX(self): return self.x
    def getY(self): return self.y
    def getZ(self): return self.z

    def setX(self, value):
        self.X = value

    def setY(self, value):
        self.Y = value

    def setZ(self, value):
        self.Z = value

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        _crossX = self.y * other.z - self.z * other.y
        _crossY = self.z * other.x - self.x * other.z
        _crossZ = self.x * other.y - self.y * other.x
        return Vecotr3D(_crossX, _crossY, _crossZ)

    def are_orthogonal(vectorOne, vectorTwo):
        if vectorOne.dot(vectorTwo) == 0:
            return True
        else
            return False





