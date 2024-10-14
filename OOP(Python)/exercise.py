import numpy as np

# Create the first row: reverse order of the even integers from 2 through 10
first_row = [x for x in range(10, 1, -2)]

# Create the second row: odd integers from 1 through 9
second_row = [x for x in range(1, 10, 2)]

# Combine the two rows into a 2-by-5 array
output = np.array([first_row, second_row])

# Display the resulting array
print(output)
