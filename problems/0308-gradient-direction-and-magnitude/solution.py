import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	
import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    """
    mag = np.linalg.norm(gradient)

    # Handle the zero vector
    if mag == 0:
        return {
            "magnitude": 0.0,
            "direction": [0.0] * len(gradient),
            "descent_direction": [0.0] * len(gradient)
        }

    # Direction of steepest ascent
    dire = [i / mag for i in gradient]

    # Direction of steepest descent
    des_dir = [-i for i in dire]

    return {
        "magnitude": float(mag),
        "direction": dire,
        "descent_direction": des_dir
    }
