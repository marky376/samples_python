def generate_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # You can customize the way elements are generated here
            element = i * cols + j + 1
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example: Generate a 3x3 matrix
rows = 3
cols = 3
my_matrix = generate_matrix(rows, cols)

# Print the generated matrix
print("Generated Matrix:")
print_matrix(my_matrix)

