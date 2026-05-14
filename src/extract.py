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
    except ValueError:
        raise ValueError(f"Invalid CSV format in file {file_path}")
    except Exception as e:

        raise Exception(f"Error occurred while extracting data from {file_path}: {e}")
    
    return df