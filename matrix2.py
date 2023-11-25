import numpy as np
import matplotlib.pyplot as plt

def generate_colorful_matrix(rows, cols):
    matrix = np.random.rand(rows, cols)  # Generate a matrix of random values between 0 and 1
    return matrix

def plot_colorful_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Values')
    plt.title('Colorful Matrix')
    plt.show()

# Example: Generate and plot a colorful matrix
rows = 5
cols = 5
colorful_matrix = generate_colorful_matrix(rows, cols)

plot_colorful_matrix(colorful_matrix)

