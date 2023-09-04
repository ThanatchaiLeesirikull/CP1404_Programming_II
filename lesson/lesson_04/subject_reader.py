import matplotlib.pyplot as plt

STheta = [25.649, 25.656, 25.654, 25.643, 25.643, 25.651, 25.658, 25.682, 25.71, 25.801, 25.819, 25.9, 25.975, 26.043]
Depthm = [0, 8, 10, 19, 20, 30, 39, 50, 58, 75, 78, 100, 117, 125]

plt.figure(figsize=(10, 6))

# Create the histogram
plt.hist(STheta, bins=10, color='blue', edgecolor='black')

plt.xlabel('Water density (kg/m^3)')
plt.ylabel('Frequency')
plt.title('Histogram of STheta')
plt.grid(True)
plt.show()
