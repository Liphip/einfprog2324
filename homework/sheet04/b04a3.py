# Philip Laskowicz

def intSuperliste(liste: list) -> bool:
    """
    Checks if the given list is an int-superlist recursively.
    A int-superlist is a list where either every element is an integer
    or every element is another int-superlist.

    Parameters
    ----------
    liste : list
        The list to check.

    Returns
    -------
    bool
        True if the list is an int-superlist, False otherwise.
    """
    # TODO: Clarify if 'all' and 'isinstance' are allowed.
    #       If so, this can be done in less lines.
    ## Base case.
    # if all(isinstance(element, int) for element in liste):
    #     return True
    ## Recursive case.
    # if all(isinstance(element, list) for element in liste):
    #     return all(intSuperliste(element) for element in liste)
    # return False

    prev_int = False
    for element in liste:
        # Base case.
        if type(element) == int:
            prev_int = True
        # Recursive case.
        else:
            if prev_int or type(element) != list or not intSuperliste(element):
                return False
    return True




def kopie(intSuperliste: list) -> list:
    """
    Creates a copy of the given int-superlist recursively.

    Parameters
    ----------
    intSuperliste : list
        The int-superlist to copy.

    Returns
    -------
    list
        The copy of the int-superlist.
    """
    # Base case.
    # Since the list is an int-superlist, when the first element is an integer,
    # the whole list is an integer list.
    if type(intSuperliste[0]) == int:
        return intSuperliste.copy()
    # Recursive case.
    return [kopie(element) for element in intSuperliste]


if __name__ == "__main__":
    S=[1,2,3]
    K=[[1,2,4,5],S]
    M=[1,2,[3,6]]
    L=[K,[[2,3]],[S,[1,2]]]
    print(intSuperliste(S))
    print(intSuperliste(K))
    print(intSuperliste(L))
    print(intSuperliste(M))
    V=kopie(S)
    W=kopie(K)
    U=kopie(L)
    print(V)
    print(W)
    print(U)
    S.append(5)
    print(V)
    print(W)
    print(U)
