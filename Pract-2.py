import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
mean = 0          # Mean of the distribution
std_dev = 1       # Standard deviation of the distribution
sample_size = 5000 # Number of samples

# Generate normal distribution data
data = np.random.normal(mean, std_dev, sample_size)

# Calculate statistics
calculated_mean = np.mean(data)
calculated_std_dev = np.std(data)

print(f"Mean: {calculated_mean:.2f}")
print(f"Standard Deviation: {calculated_std_dev:.2f}")

# Plotting
plt.figure(figsize=(10, 6))

# Histogram and density plot using seaborn
sns.histplot(data, bins=30, kde=True, color='skyblue', stat="density")

# Plot normal distribution curve using scipy.stats.norm
x = np.linspace(min(data), max(data), 1000)
plt.plot(x, norm.pdf(x, calculated_mean, calculated_std_dev), color='red', linewidth=2, label='Normal Distribution')

# Adding labels and title
plt.title("Typical Normal Data Distribution")
plt.xlabel("Data Values")
plt.ylabel("Density")
plt.legend()

# Show the plot
plt.show()
