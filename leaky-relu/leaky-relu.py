import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    relu = np.maximum(0,x)
    inv_relu = np.minimum(0,x)
    leaky_relu = relu + alpha * inv_relu
    return leaky_relu
    
        
    