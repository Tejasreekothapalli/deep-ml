import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	return np.real_if_close(np.linalg.eigvals(matrix))