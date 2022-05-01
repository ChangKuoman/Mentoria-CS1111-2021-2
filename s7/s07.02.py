
### INTRODUCCION ###

# imagenes

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Abriendo la imagen
image = Image.open("babyyoda.jpg")
matrix = np.array(image, dtype='int')

print(matrix.shape)
(f, c, d) = matrix.shape

# Pintando la imagen
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        r, g, b = matrix[i][j]
        if i < len(matrix)//2 and j < len(matrix[0])//2:
            matrix[i][j] = [r, 0, 0]
        elif i < len(matrix)//2 and j > len(matrix[0])//2:
            matrix[i][j] = [0, 0, b]
        elif i > len(matrix)//2 and j < len(matrix[0])//2:
            matrix[i][j] = [r, g, b]
        else:
            matrix[i][j] = [0, g, 0]

# Mostrando la imagen
plt.imshow(matrix[::])
plt.show()
