import numpy as np
arr1 = np.array([1, 2, 3])
print(arr1*2)

l = [1, 2, 3]
l2=[]
for i in range(len(l)):
    x= l[i]*2
    l2.append(x)
print(l2)


# Q2. Develop a Python program using NumPy to create one-dimensional and two-dimensional arrays, and display their shape, dimensions, and data type.


# One-dimensional array
arr1 = np.array([1,2,3,4,5])
print(f"One-D Array:-{arr1}")
print(f"Shape:-{arr1.shape}")
print(f"Dimensions:-{arr1.ndim}")
print(f"Data type:-{arr1.dtype}")

# Two-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:-{arr2}")
print(f"Shape:-{arr2.shape}")
print(f"Dimensions:-{arr2.ndim}")
print(f"Data type:-{arr2.dtype}")
