# ex_5_2.py
import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


def main():
    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Load data from the input file
    data = np.loadtxt(INFILE, delimiter=',')  # Assuming the file is CSV with comma as delimiter

    # Print the mean and standard deviation of the original data
    print("Original Data:")
    print("Mean:", np.mean(data))
    print("Standard Deviation:", np.std(data))

    # Modify the input data so that it has a mean of 0
    zero_mean_data = data - np.mean(data, axis=0)

    # Modify the zero mean data so that it has a standard deviation of 1
    processed = zero_mean_data / np.std(zero_mean_data, axis=0)

    # Print the mean and standard deviation of the processed data
    print("\nProcessed Data:")
    print("Mean:", np.mean(processed))
    print("Standard Deviation:", np.std(processed))

    # Save the processed data to the specified output file
    np.savetxt(OUTFILE, processed, fmt="%.6f", delimiter=",")  # Save the processed data

    # Load the saved data and print it
    loaded_data = np.loadtxt(OUTFILE, delimiter=",")  # Load the processed data
    print("\nLoaded Data:")
    print(loaded_data)


if __name__ == "__main__":
    main()
