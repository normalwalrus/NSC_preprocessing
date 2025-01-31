import os
import io
import json

def export_list_to_json(path_to_output, data):

    with open(path_to_output, 'w') as final:
        json.dump(data, final)
