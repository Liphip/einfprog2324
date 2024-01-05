import random

# a)
def matrix_mult(L1: list, L2: list) -> list or None:
    """
    Calculates the product of the two given matrices.
    Returns None if the matrices cannot be multiplied.

    Parameters:
    ----------
        L1 (list): First matrix.
        L2 (list): Second matrix.

    Returns:
    -------
        list: The product of the two given matrices.
        None: If the matrices cannot be multiplied.
    """

    def is_integer_matrix(L: list) -> bool:
        """
        Checks if the given matrix is an integer matrix.

        Parameters:
        ----------
            L (list): Matrix.

        Returns:
        -------
            bool: True if the given matrix is an integer matrix, False otherwise.
        """
        inner_list_length = len(L[0])
        for row in L:
            if not isinstance(row, list):
                return False
            if len(row) != inner_list_length:
                return False
            for elem in row:
                if not isinstance(elem, int):
                    return False
        return True

    def is_compatible(L1: list, L2: list) -> bool:
        """
        Checks if the given matrices are compatible for multiplication.

        Parameters:
        ----------
            L1 (list): First matrix.
            L2 (list): Second matrix.

        Returns:
        -------
            bool: True if the given matrices are compatible for multiplication, False otherwise.
        """
        if not is_integer_matrix(L1) or not is_integer_matrix(L2):
            return False
        if len(L1[0]) != len(L2):
            return False
        return True

    def print_matrix(L: list) -> None:
        """
        Prints the given matrix to the console.

        Parameters:
        ----------
            L (list): Matrix.

        Returns:
        -------
            None
        """
        if not is_integer_matrix(L):
            print("Keine Matrix")
            return
        for row in L:
            print(" ".join(map(str, row)))
    
    if not is_compatible(L1, L2):
        print("Keine Multiplikation möglich")
        return 
    
    # Calculate the product of the two matrices.
    product = []

    for row in L1:
        new_row = []
        for column in zip(*L2):
            new_row.append(sum([i * j for i, j in zip(row, column)]))
        product.append(new_row)

    print_matrix(product)
    return product        

# b)
def generate_matrix(k:int, l:int, i:int, j:int)->list:
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
    return [[random.randint(i,j) for _ in range(l)] for _ in range(k)]

if __name__ == "__main__":
    # Random matrices of different sizes.
    for i in range(5):
        k = random.randint(1, 5)
        l = random.randint(1, 5)
        i, j = sorted([random.randint(-10, 10) for _ in range(2)])
        matrix_1 = generate_matrix(k, l, i, j)
        matrix_2 = generate_matrix(l, k, i, j)
        matrix_mult(matrix_1, matrix_2)
        print("")
    
    # Self-defined matrices.
    matrix_1 = [[1, 2, 3], [4, 5, 6]]
    matrix_2 = [[1, 2], [3, 4], [5, 6]]
    matrix_mult(matrix_1, matrix_2)
    print("")

    matrix_1 = [[1, 2, 3], [4, 5, 6]]
    matrix_2 = [[1, 2], [3, 4]]
    matrix_mult(matrix_1, matrix_2)
    print("")

    matrix_1 = [[1, 2], [3, 4]]
    matrix_2 = [[1, 2], [3, 4]]
    matrix_mult(matrix_1, matrix_2)
    print("")