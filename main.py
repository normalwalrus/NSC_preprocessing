from utils.NSC_preprocessing import apply_rules
from utils.unzipping import extract_from_zip_file
from utils.export import export_list_to_json
from pathlib import Path

import json
import os

DATASET = 'NSC-samples/SAME'

PATH_TO_DATA = 'data/' + DATASET
PATH_TO_OUTPUT_UNZIPPED = 'unzipped/' + DATASET
PATH_TO_OUTPUT_PROCESSED = 'processed'

PATH_TO_TEXT_DATA = PATH_TO_OUTPUT_UNZIPPED + '/TEXT'
MINIMUM_CHAR = 10

PATH_TO_OUTPUT_MANIFEST = PATH_TO_OUTPUT_PROCESSED+"/manifest.json"
PATH_TO_OUTPUT_REJECTS = PATH_TO_OUTPUT_PROCESSED+"/rejects.json"

def main():
    
    extract_from_zip_file(PATH_TO_DATA, PATH_TO_OUTPUT_UNZIPPED)
    list_of_text_data = list(Path(PATH_TO_TEXT_DATA).glob('*.txt'))

    preprocessed_list = []
    reject_list = []
    
    for text in list_of_text_data:
        
        text_name = text.name
        text_data = text.read_text()
        
        text = apply_rules(text_data, MINIMUM_CHAR)
        
        if text.split("@")[0] == 'REJECT':
            reject_entry = {"pair_id": text_name.split('.')[0], "reject_reason":text.split("@")[1], "text": text.split("@")[2]}
            reject_list.append(reject_entry)
            continue
        
        text_entry = {"pair_id": 'WAVE/'+text_name.split('.')[0]+'.wav', "text": text}
        
        preprocessed_list.append(text_entry)
    
    export_list_to_json(PATH_TO_OUTPUT_MANIFEST, preprocessed_list)
    export_list_to_json(PATH_TO_OUTPUT_REJECTS, reject_list)


if __name__ == "__main__":
    
    main()