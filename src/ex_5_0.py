# ex_5_0.py

from pathlib import Path

def line_count(infile):
    try:
        with open(infile, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(num_lines)  # Print only the line count
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Import the utility function
    from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_0_fixture.txt")
