import sys
import pandas as pd
import matplotlib
import numpy as np
import scipy as sp
import IPythin
from sklearn.datasets import import load_iris
iris_dataset = load_iris()
from sklearn import .model_selection import tain_test_split


X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'],random_state=0)

iris_dataframe = pd.DataFrame(X_train, colmns=iris_dataset_.feature_names)





