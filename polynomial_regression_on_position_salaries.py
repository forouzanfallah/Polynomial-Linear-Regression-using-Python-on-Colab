# -*- coding: utf-8 -*-
"""polynomial_regression_on_position_salaries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aIlMf5n_gDRM0q0cKmW7-aKj85MW2X8v

#🌸 Forouzan Fallah 🌸

Github: Forouzanfallah

Personal Website: Forouzanfallah.ir

Don't hesitate to contact me for any further questions ☺

# Polynomial Regression

we call it "Polynomial **Linear** Regression"
because the relation between the Y and the coefficients which we want to learn (and are our unknowns) is a linear relation.

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Position_Salaries.csv')

"""##Separate the features and the label"""

X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

"""as you can see, our data set is not linear and has curve or something that make us not to use simple regression"""

plt.scatter(X, y, color = 'magenta')

plt.show()

"""## Training the Polynomial Regression model on the dataset

Generate polynomial and interaction features.

Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree. [1, x, x^2, x^3,x^4,...].
"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
lin_regressor = LinearRegression()
poly_regressor = PolynomialFeatures(degree = 4)
X_poly = poly_regressor.fit_transform(X)
poly_regressor.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

"""## Visualising the Polynomial Regression results"""

plt.scatter(X, y, color = 'magenta')
plt.plot(X, lin_reg_2.predict(X_poly), color = 'cyan')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

"""## Predicting a new result with Polynomial Regression"""

lin_reg_2.predict(poly_reg.fit_transform([[9]]))