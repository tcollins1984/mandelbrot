import numpy as np
import matplotlib.pyplot as plt

def radius(z):
    '''
    Calculates the distance from the origin in the complex plane.'''
    return np.sqrt(z.real**2 + z.imag**2)

def angle(z):
    '''
    Calculates the angle in radians from the positive x-axis in the complex plane.
    '''   
    return np.arctan2(z.imag, z.real)
def has_converged(points, ratio_tolerance=1e-3, epsilon=1e-6):
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
    for i in range(1, len(points)):
        # Compute the magnitude ratio
        ratio = abs(points[i]) / (abs(points[i - 1]) + epsilon)
        
        # Check if the ratio suggests divergence
        if ratio > 1 + ratio_tolerance:
            return False  # Diverging if the ratio exceeds 1 significantly
    return True  # Converging or stationary if all ratios are <= 1

def julia_process(z,c=0,steps=10):
    '''
    Generates a sequence of complex numbers based on the Julia set iteration algorithm
    with default c=0.'''
    points = []
    for i in range(steps):
        z = z**2 + c
        points.append(z)
    real = [z.real for z in points]
    imaginary = [z.imag for z in points]
    # print(points)
    converges = has_converged(points)
    return points,real,imaginary,converges

js = julia_process(0.2+.2j,steps=20,c=0)
plt.figure(figsize=(10,10))
for i in range(len(js[1]) - 1):
    # Arrow ends precisely at the next point
    plt.annotate(
        '', 
        xy=(js[1][i + 1], js[2][i + 1]),   # End point of the arrow
        xytext=(js[1][i], js[2][i]),       # Start point of the arrow
        arrowprops=dict(
            arrowstyle='->',
            color='blue',
            lw=1.5,  # Line width
            shrinkA=1, shrinkB=1  # Disable shrinking to keep arrow precise
        )
    )

# Add labels, grid, and title
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Complex Plane - Julia Set Trajectory')
plt.figtext(s=f'Converges: {js[3]}', x=.5, y=.75, fontsize=12)
plt.grid(True)
plt.legend()
plt.axis('equal')  # Equal scaling for both axes
plt.show()