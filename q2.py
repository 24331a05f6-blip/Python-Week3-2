import numpy as np
a = np.ndarray(shape=(3,3), dtype=int)
a[0][0]=9
a[0][1]=8
a[0][2]=7
a[1][0]=6
a[1][1]=5
a[1][2]=4
a[2][0]=3
a[2][1]=2
a[2][2]=1
print("matrix1 elements are: \n",a)
print("dimension of matrix1 is: ",a.ndim)
b=np.ndarray(shape=(3,3), dtype=int)
b[0][0]=2
b[0][1]=4
b[0][2]=6
b[1][0]=8
b[1][1]=10
b[1][2]=12
b[2][0]=14
b[2][1]=16
b[2][2]=18
print("matrix2 elemnts are: \n",b)
print("dimension of matrix2 is: ",b.ndim)
print("addition of two matrixes are: \n",np.add(a,b))
print("subtraction of two matrixes are: \n",np.subtract(a,b))
print("matrix multplication of two matrices are: \n",np.dot(a,b))
print("Divison of two matrixes are: \n",np.divide(a,b))
