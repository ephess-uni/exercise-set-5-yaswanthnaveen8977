"""ex_5_1.py"""
import argparse  # Make sure to import the argparse module

try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)

# Entry point for command-line execution
if __name__ == "__main__":
    # Instantiate an ArgumentParser object
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

    # Add a positional argument for the input file
    parser.add_argument("infile", help="The input file to count lines.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the infile argument
    main(args.infile)
