import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    # Transform C to a numpy list
    O = np.array(C).copy()
    
    R_i = np.sum(C , axis = 1) # Row totals 
    C_j = np.sum(C , axis = 0) # Column totals
    N = np.sum(C) # Grand total
    E_ij = np.outer(R_i , C_j) / N # Expected Frequencies Under Independence

    # The Chi-Square Test Statistic
    X_2 = (((O - E_ij) ** 2)/E_ij).sum()
    
    #Degrees of Freedom
    df = (O.shape[0] - 1) * (O.shape[1] - 1)
    result = {"chi2": float(X_2), "expected": E_ij}
    return result