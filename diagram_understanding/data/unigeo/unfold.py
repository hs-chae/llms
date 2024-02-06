import json
import numpy as np
import base64
import pickle


def ndarray_to_base64(ndarray):
    """
    Convert a numpy ndarray to a base64 encoded string.
    """
    return base64.b64encode(ndarray).decode('utf-8')


def convert_to_serializable(obj):
    """
    Convert non-serializable objects to a serializable format.
    """
    if isinstance(obj, np.ndarray):
        # Convert numpy arrays to base64 encoded strings
        return ndarray_to_base64(obj)
    elif isinstance(obj, set):
        # Convert sets to lists
        return list(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)


def process_data(file_path, output_file_path):
    """
    Load data from a pickle file, process it to convert non-serializable objects,
    and save it as a JSON file.
    """
    # Load the data from the pickle file
    with open(file_path, 'rb') as file:
        data = pickle.load(file)

    # Convert the data to a serializable format
    serializable_data = [convert_to_serializable(item) for item in data]

    # Write the serializable data to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(serializable_data, json_file, default=convert_to_serializable, ensure_ascii=False, indent=2)


pk_path = 'diagram_understanding/data/unigeo'
# Paths to the input pickle files and output JSON files
train_file_path = 'calculation_test.pk'
train_json_output_file_path = 'path_to_calculation_train_result.json'
test_file_path = 'path_to_proving_test.pk'
test_json_output_file_path = 'path_to_proving_test_result.json'

# Process each file
process_data(train_file_path, train_json_output_file_path)
process_data(test_file_path, test_json_output_file_path)
