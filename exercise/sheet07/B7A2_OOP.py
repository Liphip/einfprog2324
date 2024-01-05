# Not the correct solution for the exercise, but a good example for the usage of classes.
# This problem is very good for the usage of classes, because matrices are a very common mathematical object.
import random
import typing

class IntegerMatrix:
    """
    Represents an integer matrix.

    Attributes:
    ----------
        matrix (list): Matrix.
        rows (int): Number of rows.
        columns (int): Number of columns.

    Methods:
    -------
        is_integer_matrix(matrix:list) -> bool
        __init__(matrix:list) -> None
    """

    @classmethod
    def __is_integer_matrix__(cls, matrix:list) -> bool:
        """
        Checks if the given matrix is an integer matrix.

        Parameters:
        ----------
            matrix (list): Matrix.

        Returns:
        -------
            bool: True if the given matrix is an integer matrix, False otherwise.
        """
        inner_list_length = len(matrix[0])
        for row in matrix:
            if not isinstance(row, list):
                return False
            if len(row) != inner_list_length:
                return False
            for elem in row:
                if not isinstance(elem, int):
                    return False
        return True
    
    @classmethod
    def __is_compatible__(cls, matrix_1:list, matrix_2:list) -> bool:
        """
        Checks if the given matrices are compatible for multiplication.

        Parameters:
        ----------
            matrix_1 (list): First matrix.
            matrix_2 (list): Second matrix.

        Returns:
        -------
            bool: True if the given matrices are compatible for multiplication, False otherwise.
        """
        if not cls.__is_integer_matrix__(matrix_1) or not cls.__is_integer_matrix__(matrix_2):
            return False
        if len(matrix_1[0]) != len(matrix_2):
            return False
        return True
    
    @classmethod
    def __generate_matrix__(cls, k:int, l:int, i:int, j:int)->'IntegerMatrix':
        """
        Generates a (k,l)-matrix with random integer entries between i and j.

        Parameters:
        ----------
            k (int): Number of rows.
            l (int): Number of columns.
            i (int): Lower bound for random integer entries.
            j (int): Upper bound for random integer entries.

        Returns:
        -------
            list: The generated matrix.
        """
        return cls([[random.randint(i,j) for _ in range(l)] for _ in range(k)])

    def __init__(self, matrix:list) -> None:
        """
        Initializes the IntegerMatrix class.
        """
        if not IntegerMatrix.__is_integer_matrix__(matrix):
            raise TypeError("The given matrix is not an integer matrix.")
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def is_compatible(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the given matrix is compatible for multiplication.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the given matrix is compatible for multiplication, False otherwise.
        """
        return IntegerMatrix.__is_compatible__(self.matrix, other.matrix)
    
    def get_matrix(self) -> list:
        """
        Returns the matrix.

        Returns:
        -------
            list: The matrix.
        """
        return self.matrix
    
    def get_rows(self) -> int:
        """
        Returns the number of rows.

        Returns:
        -------
            int: The number of rows.
        """
        return self.rows
    
    def get_columns(self) -> int:
        """
        Returns the number of columns.

        Returns:
        -------
            int: The number of columns.
        """
        return self.columns
    
    def print_matrix(self) -> None:
        """
        Prints the given matrix to the console.

        Returns:
        -------
            None
        """
        if not IntegerMatrix.__is_integer_matrix__(self.matrix):
            print("Keine Matrix")
            return
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def __str__(self) -> str:
        """
        Returns a string representation of the matrix.

        Returns:
        -------
            str: String representation of the matrix.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])
    
    def __add__(self, other: 'IntegerMatrix') -> list:
        """
        Adds the two matrices.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            list: The sum of the two matrices.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("The matrices cannot be added.")
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
    
    def __sub__(self, other: 'IntegerMatrix') -> list:
        """
        Subtracts the two matrices.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            list: The difference of the two matrices.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("The matrices cannot be subtracted.")
        return [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
    
    def __mul__(self, other: 'IntegerMatrix') -> list:
        """
        Multiplies the two matrices.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            list: The product of the two matrices.
        """
        if self.columns != other.rows:
            raise ValueError("The matrices cannot be multiplied.")
        return [[sum([i * j for i, j in zip(self.matrix[row], column)]) for column in zip(*other.matrix)] for row in range(self.rows)]
    
    def __eq__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the two matrices are equal.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the two matrices are equal, False otherwise.
        """
        if self.rows != other.rows or self.columns != other.columns:
            return False
        return self.matrix == other.matrix
    
    def __ne__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the two matrices are not equal.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the two matrices are not equal, False otherwise.
        """
        return not self == other
    
    def __lt__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the first matrix is less than the second matrix.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the first matrix is less than the second matrix, False otherwise.
        """
        return self.rows < other.rows or self.columns < other.columns
    
    def __le__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the first matrix is less than or equal to the second matrix.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the first matrix is less than or equal to the second matrix, False otherwise.
        """
        return self.rows <= other.rows or self.columns <= other.columns
    
    def __gt__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the first matrix is greater than the second matrix.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the first matrix is greater than the second matrix, False otherwise.
        """
        return self.rows > other.rows or self.columns > other.columns
    
    def __ge__(self, other: 'IntegerMatrix') -> bool:
        """
        Checks if the first matrix is greater than or equal to the second matrix.

        Parameters:
        ----------
            other (IntegerMatrix): The other matrix.

        Returns:
        -------
            bool: True if the first matrix is greater than or equal to the second matrix, False otherwise.
        """
        return self.rows >= other.rows or self.columns >= other.columns
    
    def __getitem__(self, key: typing.Tuple[int, int]) -> int:
        """
        Returns the element at the given index.

        Parameters:
        ----------
            key (tuple): Index.

        Returns:
        -------
            int: Element at the given index.
        """
        return self.matrix[key[0]][key[1]]
    
    def __setitem__(self, key: typing.Tuple[int, int], value: int) -> None:
        """
        Sets the element at the given index to the given value.

        Parameters:
        ----------
            key (tuple): Index.
            value (int): Value.
        """
        self.matrix[key[0]][key[1]] = value

if __name__ == "__main__":
    # Random matrices of different sizes.
    for i in range(5):
        k = random.randint(1, 5)
        l = random.randint(1, 5)
        i, j = sorted([random.randint(-10, 10) for _ in range(2)])
        matrix_1 = IntegerMatrix.__generate_matrix__(k, l, i, j)
        matrix_2 = IntegerMatrix.__generate_matrix__(l, k, i, j)
        print(matrix_1 * matrix_2)
        print("")
    
    # Self-defined matrices.
    matrix_1 = IntegerMatrix([[1, 2, 3], [4, 5, 6]])
    matrix_2 = IntegerMatrix([[1, 2], [3, 4], [5, 6]])
    print(matrix_1 * matrix_2)
    print("")

    matrix_1 = IntegerMatrix([[1, 2, 3], [4, 5, 6]])
    matrix_2 = IntegerMatrix([[1, 2], [3, 4]])
    print(matrix_1 * matrix_2)
    print("")

    matrix_1 = IntegerMatrix([[1, 2], [3, 4]])
    matrix_2 = IntegerMatrix([[1, 2], [3, 4]])
    print(matrix_1 * matrix_2)
    print("")