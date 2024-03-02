"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths.  Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"

# Process the input data using numpy

# Save the result to output_file
def process_and_save_data():
    # Get the root directory of the repository
    root_directory = Path(__file__).resolve().parent.parent

    # Define the input and output file paths
    infile = root_directory / 'data' / 'ex_5_4-data.csv'
    outfile = root_directory / 'outputs' / 'ex_5_4-processed.csv'

    # Load the 1000-element ndarray from the input file
    data = np.loadtxt(infile, delimiter=',')

    # Set any negative elements of the array to 0
    processed_data = np.maximum(data, 0)

    # Write the processed array to the output file
    np.savetxt(outfile, processed_data, fmt="%.6f", delimiter=',')

if __name__ == "__main__":
    process_and_save_data()

