"""ex_5_0.py"""

def line_count(infile):
    try:
        with open(infile, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"The file '{infile}' has {num_lines} lines.")
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Adjust the import based on your file structure
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
