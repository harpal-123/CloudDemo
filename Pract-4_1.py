import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a linear regression object and fit the data
lr_model = LinearRegression()
lr_model.fit(X, y)

# Get the coefficients
m = lr_model.coef_[0][0]
b = lr_model.intercept_[0]

# Create a range of x values for the line
x_range = np.linspace(X.min(), X.max(), 100)

# Calculate the corresponding y values
y_range = m * x_range + b

# Create the plot
plt.scatter(X, y, label='Data points')
plt.plot(x_range, y_range, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
