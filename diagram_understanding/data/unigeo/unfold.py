from PIL import Image
import os
import pickle
import numpy as np
import json

def convert_array_to_image(array, image_index):
    """Converts a NumPy array to an image and saves it."""
    image = Image.fromarray(array.astype('uint8'))  # Convert NumPy array to PIL Image object
    image.save(f'cal_test/image_{image_index}.png')  # Save the image with the given index
    return image_index

def process_pickle_file(pickle_file_path):
    """Processes a pickle file, converting any found image arrays to image files."""
    with open(pickle_file_path, 'rb') as file:
        data = pickle.load(file)  # Deserialize the pickle file

        # Iterate through the deserialized object to find image data
        for index, item in enumerate(data):
            if isinstance(item, dict) and 'image' in item:
                image_data = item['image']
                if isinstance(image_data, np.ndarray):  # Check if the 'image' key contains a NumPy array
                   item['image'] =  convert_array_to_image(image_data, index)  # Convert the array to an image file


        #Write the updated data back to the python file
        python_file_path =  os.path.splitext(pickle_file_path)[0] + '.py'
        with open(python_file_path, 'w') as file:
            file.write(repr(data))


# Replace 'your_pickle_file.pkl' with the path to your actual pickle file
process_pickle_file('calculation_test.pk')