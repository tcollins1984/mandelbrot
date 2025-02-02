import numpy as np
import matplotlib.pyplot as plt

complex_points = []
for i in range(10000):
    complex_points.append(4*(np.random.rand()-.5) + 4*(np.random.rand()-.5) * 1j)
print(complex_points)
def has_converged(complex_points, ratio_tolerance=1e-3, epsilon=1e-6):
    """
    Determine if a sequence converges using the ratio of consecutive magnitudes.

    Parameters:
    - points: List of complex numbers representing the sequence.
    - ratio_tolerance: Maximum acceptable deviation of ratios for convergence (default is 1e-3).
    - epsilon: Small constant to prevent division by zero (default is 1e-6).

    Returns:
    - True if the sequence converges or stabilizes.
    - False if the sequence diverges.
    """
    for i in range(1, len(complex_points)):
        # Compute the magnitude ratio
        ratio = abs(complex_points[i]) / (abs(complex_points[i - 1]) + epsilon)
        
        # Check if the ratio suggests divergence
        if ratio > 1 + ratio_tolerance:
            return False  # Diverging if the ratio exceeds 1 significantly
    return True  # Converging or stationary if all ratios are <= 1

def julia_process(z,c=0,steps=10):
    points = []
    try:
        for i in range(steps):
            z = pow(z,2) + c
            points.append(z)
    except OverflowError:
        pass
    
    # print(points)
    converges = has_converged(points)
    return points,converges

def points_in_mandelbrot(complex_points):
    mandelbrot_points = []
    for point in complex_points:
        if julia_process(point)[1]:
            mandelbrot_points.append(point)
    real = [x.real for x in mandelbrot_points]
    imaginary = [x.imag for x in mandelbrot_points]
    return real, imaginary

    
print(points_in_mandelbrot(complex_points))
# Add labels, grid, and title
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.scatter(points_in_mandelbrot(complex_points)[0],points_in_mandelbrot(complex_points)[1], color='red')
plt.title('Complex Plane - Mandelbrot Set')
plt.axis('equal')  # Equal scaling for both axes
plt.show()