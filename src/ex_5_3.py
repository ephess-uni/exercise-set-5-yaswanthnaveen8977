# ex_5_3.py
import numpy as np
from argparse import ArgumentParser

def main(infile, outfile):
    # Load data from the input file
    data = np.loadtxt(infile, delimiter=',')

    # Modify the input data so that it has a mean of 0
    zero_mean_data = data - np.mean(data, axis=0)

    # Modify the zero mean data so that it has a standard deviation of 1
    processed = zero_mean_data / np.std(zero_mean_data, axis=0)

    # Save the processed data to the specified output file
    np.savetxt(outfile, processed, fmt="%.6f", delimiter=",")

if __name__ == "__main__":
    # Instantiate an ArgumentParser object
    parser = ArgumentParser(
        description="This program applies a standard scale transform to the data in infile and writes it to outfile."
    )

    # Add positional arguments for input and output files
    parser.add_argument("infile", help="Input filename for the data file that needs to be processed.")
    parser.add_argument("outfile", help="Output filename for the processed data.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the infile and outfile arguments
    main(args.infile, args.outfile)
