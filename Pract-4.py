import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: student marks
hours_studied = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
marks = np.array([40, 50, 60, 70, 80, 85, 90, 92, 95, 98])

# Reshape the data to be 2D
hours_studied = hours_studied.reshape(-1, 1)

# Create a linear regression object and fit the data
lr_model = LinearRegression()
lr_model.fit(hours_studied, marks)

# Get the coefficients
m = lr_model.coef_[0]
b = lr_model.intercept_

# Create a range of x values for the line
x_range = np.linspace(hours_studied.min(), hours_studied.max(), 100)

# Calculate the corresponding y values
y_range = m * x_range + b

# Create the plot
plt.scatter(hours_studied, marks, label='Student Marks')
plt.plot(x_range, y_range, color='red', label='Linear Regression')
plt.xlabel('Hours Studied')
plt.ylabel('Marks')
plt.title('Linear Regression for Student Marks')
plt.legend()
plt.show()
