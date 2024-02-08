import matplotlib.pyplot as plt

# Define the start and end points for two lines
# Line 1 points
x1_start, y1_start = (1, 2)  # Starting point for Line 1
x1_end, y1_end = (4, 3)     # Ending point for Line 1

# Line 2 points
x2_start, y2_start = (1, 3)  # Starting point for Line 2
x2_end, y2_end = (4, 1)     # Ending point for Line 2

# Plot Line 1
plt.plot([x1_start, x1_end], [y1_start, y1_end], label='Line 1', marker='o')

# Plot Line 2
plt.plot([x2_start, x2_end], [y2_start, y2_end], label='Line 2', marker='o')

# Add labels and legend
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Two Lines')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
