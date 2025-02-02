import numpy as np
import matplotlib.pyplot as plt

candidates_for_mandelbrot = []
for i in range(100000):
    candidates_for_mandelbrot.append(4*(np.random.rand()-0.5) + 4*(np.random.rand()-.5) * 1j)
print(candidates_for_mandelbrot)

def mandelbrot_process(c,z=0,steps=1000):
    
    for _ in range(steps):
        z = pow(z,2) + c
        if abs(z) > 2:
            return False # Diverging if the magnitude exceeds 2
        
    return True
   
    


def points_in_mandelbrot(complex_points):
    mandelbrot_points = [point for point in complex_points if mandelbrot_process(point)]
    
    real = [x.real for x in mandelbrot_points]
    imaginary = [x.imag for x in mandelbrot_points]
    return real, imaginary

real_part, imaginary_part = points_in_mandelbrot(candidates_for_mandelbrot) 
print(points_in_mandelbrot(candidates_for_mandelbrot))
# Add labels, grid, and title
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.scatter(real_part,imaginary_part, color='red', s=1)
plt.title('Complex Plane - Mandelbrot Set')
plt.axis('equal')  # Equal scaling for both axes
plt.show()