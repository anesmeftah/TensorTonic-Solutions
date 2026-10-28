import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    n = X.shape[0]
    
    w = np.zeros(X.shape[1])
    b = 0.0

    for step in range(steps) :
        

        z = X @ w + b
        p = _sigmoid(z)
        
        dw = (1/n) * X.T @ (p-y)
        db = np.mean(p-y)

        w = w - lr * dw
        b = b - lr * db
    
    return (w,b)
        
    