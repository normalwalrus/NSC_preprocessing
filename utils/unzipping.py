import zipfile
import os
from pathlib import Path

def extract_from_zip_file(path_to_zip_folder = 'data/NSC-samples/SAME', output_directory = 'unzipped/NSC-samples/SAME'):
    """
    Unzips all files in a given directory
    """
    
    
    list_of_directories = os.listdir(path_to_zip_folder)

    for directory in list_of_directories:
        
        path_to_zip_file = path_to_zip_folder+'/'+directory

        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            
            Path(output_directory).mkdir(parents=True, exist_ok=True)
            zip_ref.extractall(output_directory)