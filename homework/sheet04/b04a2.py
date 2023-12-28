# Philip Laskowicz

def kapital(n: int)-> float:
    """
    Calculate the capital after n years recursively.
    The capital is 5000(€) and the interest rate is 5% p.a.

    Parameters
    ----------
    n : int
        The number of years.

    Returns
    -------
    float
        The capital after n years.
    """
    # Base case.
    if n == 0:
        return 5000
    # Recursive case.
    return kapital(n - 1) * 1.05

if __name__ == "__main__":
    # Get input from user.
    num_years = int(input("Please enter the number of years: "))

    # Calculate the capital after num_years years.
    kapital_n = kapital(num_years)

    # TODO: Clarify if the return value of 'kapital' really should not be printed.
    #       The task said only to call the function, not to print the return value.