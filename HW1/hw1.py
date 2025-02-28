# -*- coding: utf-8 -*-
"""HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXYFc6sXEy_fAzr_hejn-SIkeNuYb3aQ
"""

import numpy as np

"""# Q1"""

#source = "https://www.geeksforgeeks.org/how-to-compare-two-numpy-arrays/"

def element_wise_comparison(array1, array2):
    """
    Perform element-wise comparisons between two NumPy arrays.

    Parameters:
    - array1 (numpy.ndarray): First input NumPy array.
    - array2 (numpy.ndarray): Second input NumPy array.

    Returns:
    - tuple: A tuple of NumPy arrays containing the following element-wise comparison results:
        - greater_result (numpy.ndarray): Element-wise greater than comparison.
        - greater_equal_result (numpy.ndarray): Element-wise greater than or equal to comparison.
        - less_result (numpy.ndarray): Element-wise less than comparison.
        - less_equal_result (numpy.ndarray): Element-wise less than or equal to comparison.
    """
    greater_result = np.greater(array1,array2)
    greater_equal_result = np.greater_equal(array1,array2)
    less_result = np.less(array1,array2)
    less_equal_result = np.less_equal(array1,array2)

    return greater_result, greater_equal_result, less_result, less_equal_result

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[1, 2], [2, 3]])

greater, greater_equal, less, less_equal = element_wise_comparison(array1, array2)

print("Greater than:")
print(greater)
print("\nGreater than or equal to:")
print(greater_equal)
print("\nLess than:")
print(less)
print("\nLess than or equal to:")
print(less_equal)

"""# Q2"""

# source = "https://www.educative.io/blog/numpy-matrix-multiplication"

def array_multiply(array1, array2, method="element-wise"):
    """
    Perform multiplication between two NumPy arrays using the specified method.

    Parameters:
    - array1 (numpy.ndarray): First input NumPy array.
    - array2 (numpy.ndarray): Second input NumPy array.
    - method (str, optional): The multiplication method to use. Defaults to "element-wise".

    Returns:
    - numpy.ndarray: The result of the multiplication operation based on the chosen method.
    """
    if method == "matrix-multiply":
      # result = np.dot(array1,array2)
      result = np.matmul(array1,array2)
    else:
      result = np.multiply(array1,array2)

    return result

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[2, 0], [1, 2]])

# Perform element-wise multiplication
element_wise_result = array_multiply(array1, array2, method="element-wise")
print("Element-wise multiplication:")
print(element_wise_result)

# Perform matrix multiplication
matrix_multiply_result = array_multiply(array1, array2, method="matrix-multiply")
print("\nMatrix multiplication:")
print(matrix_multiply_result)

"""# Q3"""

# source = "https://www.geeksforgeeks.org/numpy-sum-in-python/"

def broadcast_add(p, q, method="row-wise"):
    """
    Perform addition between two NumPy arrays using broadcasting and the specified method.

    Parameters:
    - p (numpy.ndarray): First input NumPy array.
    - q (numpy.ndarray): Second input NumPy array.
    - method (str, optional): The addition method to use. Defaults to "row-wise".
        - "row-wise": Perform row-wise addition, broadcasting q to match the number of rows in p.
        - "column-wise": Perform column-wise addition, adding q to each column of p.

    Returns:
    - numpy.ndarray: The result of the addition operation based on the chosen method.

    Raises:
    - ValueError: If an invalid method is provided or if the shapes are incompatible for the chosen method.
    """
    n = len(q)
    new_q = np.arange(n).reshape(n,1)
    for i in range(n):
      new_q[i] = q[i]
    if method == "column-wise":
      result = np.add(p,new_q)
    else:
      result = np.add(p,q)

    return result

# Example usage with different-shaped arrays
p = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = np.array([10, 20, 30])

# Add q row-wise to p
row_wise_result = broadcast_add(p, q, method="row-wise")
print("Row-wise addition:")
print(row_wise_result)

# Add q column-wise to p
column_wise_result = broadcast_add(p, q, method="column-wise")
print("\nColumn-wise addition:")
print(column_wise_result)

"""# Q4"""

# source1 = "https://www.studytonight.com/post/creating-random-valuedarrays-in-numpy"
# source2 = "https://www.geeksforgeeks.org/how-to-normalize-an-numpy-array-so-the-values-range-exactly-between-0-and-1/"

# Initialize the random matrix
x = np.random.randint(1,11,(4,4))
y = x
z = x
print("Original Array:")
print(x)
print('------')
print(y)

print('-----------------------')

# Do the normalization
#solution1 = it is forbenius normalization
norm = np.linalg.norm(x)
x = x/norm

#solution2
y = (y - np.min(y)) / (np.max(y) - np.min(y))


print("After normalization:")
print(x)
print('----')
print(y)

"""# Q5"""

import matplotlib.pyplot as plt
import pandas as pd

# You should write your code here and print or plot the required data asked in homework documentation
df = pd.read_csv('data.csv')
# df['Closing Price']
# len(df['Date'])
daily_Returns_rate = []
daily_Returns_rate.append(df['Closing Price'][0])
for i in range(1,364):
  ouput_rate = (df['Closing Price'][i] - df['Closing Price'][i-1]) / df['Closing Price'][i-1]
  daily_Returns_rate.append(ouput_rate)
df.insert(loc=2, column="Daily Returns Rate", value=daily_Returns_rate)
# df.shift(1)
df['Daily Returns Rate'][0] = np.nan

print("1) Daily Returns : ",df['Daily Returns Rate'])

print('---------------------------------')

avg = df['Daily Returns Rate'].mean()
print("2) Average : ",avg)
print('-------------------------------')

standard_deviation = df['Daily Returns Rate'].std()
print("3) standard deviation : ",standard_deviation)

print('-------------------------------')
print("4) Closing Price plot:")
plt.plot(df['Closing Price'])
plt.show()

print('-------------------------------')
print("5) Daily Returns plot:")
plt.plot(df['Daily Returns Rate'])
plt.show()

print('-------------------------------')
print("6) minimum :",df['Daily Returns Rate'].min())
print("6) maximum : ",df['Daily Returns Rate'].max())
print('-------------------------------')

max_index = df.index[df['Closing Price'] == df['Closing Price'].max()][0]
min_index = df.index[df['Closing Price'] == df['Closing Price'].min()][0]

print("7) min price info :",df['Closing Price'][min_index],"\t",df['Date'][min_index])
print("7) max price info :",df['Closing Price'][max_index],"\t",df['Date'][max_index])

"""# Q6"""

def for_loop_feed_forward(X, w):
    """
    Perform a feed-forward operation using a for loop.

    Parameters:
    - X (numpy.ndarray): Input data matrix of shape (num_samples, num_features).
    - w (numpy.ndarray): Weight matrix of shape (num_features, 1).

    Returns:
    - numpy.ndarray: Output matrix of shape (num_samples, 1).
    """


    outputs = np.empty(shape=(X.shape[0],w.shape[1]))
    for i in range(X.shape[0]):
      for j in range(X.shape[1]):
        outputs[i] += X[i,j] * w[i]


    #### we don't use k for loop because w.shape[1] = 1
    # for i in range(X.shape[0]):
    #   for j in range(X.shape[1]):
    #     for k in range(w.shape[1]):
    #     outputs[i,k] += X[i,j] * w[i,k]

    return outputs


# source = "youtube / Basics of Deep Learning Part 5: Implementing the Feedforward Algorithm with NumPy"
def vectorized_feed_forward(X, w):
    """
    Perform a feed-forward operation using vectorization.

    Parameters:
    - X (numpy.ndarray): Input data matrix of shape (num_samples, num_features).
    - w (numpy.ndarray): Weight matrix of shape (num_features, 1).

    Returns:
    - numpy.ndarray: Output matrix of shape (num_samples, 1).
    """
    np.dot(X,w)

    return outputs

import time

# generate random samples

X =  np.random.randint(1,11,size=(3,4))
w =  np.random.randint(1,11,size=(4,1))

start_time = time.time()
outputs = for_loop_feed_forward(X, w)
print(outputs)

print("Time spent on calculating the outputs using for loops: ")
print(time.time() - start_time)

print('-----------------')
start_time = time.time()
outputs = vectorized_feed_forward(X, w)
print(outputs)

print("Time spent on calculating the outputs using vectorization: ")
print(time.time() - start_time)

"""# Q7"""

def replace_elements_above_threshold(array, threshold):
    """
    Replace elements in a NumPy array that are higher than the given threshold with a specified value.

    Parameters:
    - array (numpy.ndarray): Input NumPy array.
    - threshold (float): Threshold value to compare elements with.

    Returns:
    - numpy.ndarray: NumPy array with elements replaced above the threshold.
    """
    array[array <= threshold] = 0
    array[array > threshold] = 1
    modified_arr = array


    return modified_arr

input_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
threshold_value = 5
result_array = replace_elements_above_threshold(input_array, threshold_value)
print(result_array)

"""# Q8"""

class Matrix:
    def __init__(self, matrix):
        """
        Initialize a Matrix object with a given list of lists.

        Parameters:
        - matrix (list of lists): Input list of lists representing the matrix.
        """
        self.matrix = matrix

    def shape_comparison(self,sec_matrix):
      if len(self.matrix) != len(sec_matrix.matrix):
        return False

      for i in range(len(self.matrix)):
        if len(self.matrix[i]) != len(sec_matrix.matrix[i]):
          return False

      return True

    def is_equal(self, second_matrix):
        """
        Check if this Matrix object is equal to another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for comparison.

        Returns:
        - bool: True if the matrices are equal, False otherwise.
        """# i added a sentence for the returns

        if not self.shape_comparison(second_matrix):
          return "they don't have equal shapes -> they are not equal",False

        for i in range(len(self.matrix)):
          for j in range(len(self.matrix[i])):
            if self.matrix[i][j] != second_matrix.matrix[i][j]:
              return f"they don't have same value at position{i,j} -> they are not equal.",False

        return "they are equal",True


    #### this function didn't work properly.

    # def my_zeros_func(self):
    #   output = self.matrix
    #   for i in range(len(self.matrix)):
    #     for j in range(len(self.matrix[i])):
    #       output[i][j] = False

    #   return output


    def is_higher_elementwise(self, second_matrix):
        """
        Check if this Matrix object has higher values element-wise compared to another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for comparison.

        Returns:
        - Matrix: Matrix same shape of the input.
        """
        if not self.shape_comparison(second_matrix):
          return "they don't have same shape -> we cannot compare them"

        res = [[False for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
          for j in range(len(self.matrix[i])):
            if self.matrix[i][j] > second_matrix.matrix[i][j]:
              res[i][j] = True

        return res


    def bigger_set(self,second_matrix):
      if len(self.matrix) < len(second_matrix.matrix):
        return False
      for i in range(len(self.matrix)):
        if len(self.matrix[i]) < len(second_matrix.matrix[i]):
          return False
      return True



    def is_subset(self, second_matrix):
        """
        Check if this Matrix object is a subset of another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for comparison.

        Returns:
        - bool: True if this matrix is a subset of 'second_matrix', False otherwise.
        """
        # if self.is_equal(second_matrix):
        #   return "they are equal -> we know that equal sets are subsets of each other.",True

        # if not self.bigger_set(second_matrix):
        #     return "the second set is bigger that the first one.",False
        res = [[False for _ in range(len(second_matrix.matrix[0]))] for _ in range(len(second_matrix.matrix))]
        idx = [[0 for _ in range(len(second_matrix.matrix[0]))] for _ in range(len(second_matrix.matrix))]
        is_matrix = [[0 for _ in range(len(second_matrix.matrix[0]))] for _ in range(len(second_matrix.matrix))]

        for i in range(len(self.matrix)):
          for j in range(len(second_matrix.matrix)):
            for k in range(len(second_matrix.matrix[0])):
              if second_matrix.matrix[k][j] in self.matrix[i]:
                res[k][j] = True
                idx[k][j] = i
                is_matrix[k][j] = j


        for i in range(len(idx)):
          if len(set(idx[i])) != 1:
            return "it's not subset",False

        ls = is_matrix[0][0]
        for i in range(len(is_matrix)):
          if ls != is_matrix[i]:
            return "it's not a matrix"


        return "This matrix is a subset of the second matrix", True,res,idx,is_matrix


    def dot_product(self, second_matrix):
        """
        Calculate the dot product between this Matrix object and another Matrix object.

        Parameters:
        - second_matrix (Matrix): Another Matrix object for the dot product.

        Returns:
        - Matrix: The result of the dot product as a numpy.ndarray.
        """
        output = []
        for i in range(len(self.matrix)):
          ls = []
          for j in range(len(second_matrix.matrix[0])):
            add = 0
            for k in range(len(self.matrix[i])):
              add += self.matrix[i][k] * second_matrix.matrix[k][j]
            ls.append(add)
          output.append(ls)

        return output

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix2 = Matrix([[0, 0, 0], [4, 5, 6], [7, 8, 9]])

print(matrix1.is_equal(matrix2))

# test equality of matrices here and show the result #

matrix3 = Matrix([[0, 0, 0], [10, 20, 30], [-1, 8, 10]])
matrix3_test = Matrix([[3, -2, 4], [11, 17, 30], [-4, 18, 10]])


# test proportion of matrices here and show the result #
print(matrix3_test.is_higher_elementwise(matrix3))

matrix4 = Matrix([[5, 6], [8, 9]])
matrix5 = Matrix([[1, 2], [4, 5]])
matrix6 = Matrix([[1, 2], [3, 4]])
matrix6_test = Matrix([[1, 2], [5, 6]])




# test subset of matrices here and show the result #
print(matrix1.is_subset(matrix4))
print(matrix1.is_subset(matrix5))
print(matrix1.is_subset(matrix6))
print(matrix1.is_subset(matrix6_test))



matrix7 = Matrix([[3, 1], [2, 4], [-1, 5]])
matrix8 = Matrix([[3, 1], [2, 4]])

# test product of matrices here and show the result #
matrix7.dot_product(matrix8)