import numpy as np
import pandas as pd


input_file = "Datalogs.csv"
# comma delimited is the default
df = pd.read_csv(input_file, header = 0)

# for space delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = " ")

# for tab delimited use:
# df = pd.read_csv(input_file, header = 0, delimiter = "\t")

# put the original column names in a python list
original_headers = list(df.columns.values)

# remove the non-numeric columns

# create a numpy array with the numeric values for input into scikit-learn
numpy_array = df.as_matrix()

#print (numpy_array[0][0])
Request = 1
for i in range(len(numpy_array)):
        Request+=1
print(Request)
