import matplotlib.pyplot as plt
import numpy as np
from labels import capitals
import json

#generate random angle
def random_angle():
    return np.random.uniform(0, 2*np.pi)

random_coords = lambda: (np.random.uniform(-10, 10), np.random.uniform(-10, 10))
# Generate a random circle again



index = {}

for j in range(100):


    center = (np.random.uniform(-2,2),np.random.uniform(-2,2))  # Center of the circle remains the same
    radius = np.random.uniform(4, 10)  # Random radius between 5 and 10 units

    # Generate three random points on the circle for the triangle vertices again

    angles = [random_angle() for _ in range(3)]
    vertices = [(center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle)) for angle in angles]

    # Create a figure and a single subplot again
    fig, ax = plt.subplots()

    # Draw the circle again
    circle = plt.Circle(center, radius, edgecolor='black', facecolor='none')
    ax.add_artist(circle)

    # Draw the triangle again
    triangle = plt.Polygon(vertices, edgecolor='black', facecolor='none')
    ax.add_artist(triangle)

    # Label the center of the circle again
    ax.plot(center[0], center[1], 'o', markersize=2, markeredgecolor='black', markerfacecolor='black')
    ax.text(center[0]+0.3, center[1]+0.3, 'O', fontsize=12, ha='center', va='center')

    Labels = []

    # Label the vertices of the triangle
    for i, vertex in enumerate(vertices):
        #randomly choose a label from capitals.candidate
        while True:
            label = np.random.choice(capitals.candidates)
            if label not in Labels and  label not in ['O']:
                Labels.append(label)
                break
        ax.plot(vertex[0], vertex[1], 'o', markersize=2, markeredgecolor='black', markerfacecolor='black')
        ax.text(vertex[0]+0.3, vertex[1]+0.3, label, fontsize=12, ha='right')

    # Set equal scaling and limits to ensure the circle is properly visible
    ax.set_xlim(center[0]-radius-5, center[0]+radius+5)
    ax.set_ylim(center[0]-radius-5, center[0]+radius+5)
    ax.set_aspect('equal')

    # Remove axes again
    ax.axis('off')

    # Save the figure again
    plt.savefig(f'Second/tri_insc_circ/{j}.png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    #Save the index to json
    json_path = 'Second/tri_insc_circ/index.json'
    index[j] = {'center': center, 'radius': radius, 'vertices': vertices, 'Labels': Labels}
    with open(json_path, 'w') as json_file:
        json.dump(index, json_file, indent=4)

