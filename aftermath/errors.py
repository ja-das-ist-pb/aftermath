class MathError(Exception):
    pass

class MathInputError(MathError):
    pass

class MatrixSizeError(MathError):
    pass

class MatrixDimensionError(MathError):
    pass

class MatrixNotInvertibleError(MathError):
    pass

class VectorSizeError(MathError):
    pass

class VectorDimensionError(MathError):
    pass