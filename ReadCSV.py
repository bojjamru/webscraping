import pandas as pd
#  read csv
read = pd.read_csv("./myjobsvisa.csv")

# print(read)

read.describe()