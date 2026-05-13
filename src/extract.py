import os
import sys

import pandas as pd

def extract_csv(file_path):
    print (f"Extracting data from {file_path}...")
    
    # if os.path.getsize(file_path) < 1:
    #     print(f"Error: File {file_path} is empty.")
    #     sys.exit("Exiting due to empty file path...")
   
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")


    try:
        df = pd.read_csv(file_path)
    # except FileNotFoundError:
    #     print(f"Error: File {file_path} not found.")
    #     sys.exit("Exiting due to file not found...")
    except ValueError:
        # print(f"Error: Invalid CSV format in file {file_path}. The file may be empty or is incorrectly formatted.")
        # sys.exit("Exiting due to invalid CSV format or empty file...")
        raise ValueError(f"Invalid CSV format in file {file_path}")
    except Exception as e:
        # print(f"Error occurred while extracting data from {file_path}: {e}")
        # sys.exit("Exiting due to extraction error...")
        raise Exception(f"Error occurred while extracting data from {file_path}: {e}")
    
    return df