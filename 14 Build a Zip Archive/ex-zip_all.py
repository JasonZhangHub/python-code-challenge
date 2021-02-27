import os
import re
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):         
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root,file),
                                     arcname = os.path.join(rel_path, file))
                
    
search_dir = 'my_stuff'
extension_list = ['.jpg','.txt']
output_path='my_stuff.zip'

zip_all(search_dir, extension_list, output_path)