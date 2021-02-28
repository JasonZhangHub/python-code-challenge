import os
import re
import urllib.parse
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_files(first_url, output_dir):
    #make a directory
    if output_dir not in os.listdir():
        os.mkdir(output_dir)
        
        
    # extract image name and path to prepare for downloading
    image_name = re.findall(r"(\w+).jpg$", first_url)[0]
    image_path = re.findall(r'(.*/){}.jpg'.format(image_name), first_url)[0]

    #increment the image number. 001 --> 002 --> 003 --> 004 etc. 
    image_name_list = ['image'+ str(i).zfill(3) + '.jpg' for i in range(1000)]
    url = [image_path+i for i in image_name_list]

    for i,j  in zip(url, image_name_list):
        try:
            urllib.request.urlretrieve(i, output_dir+ '/'+j)
            print('Successfully downloaded\n {}'.format(i))
        except:
            continue

    return 

first_url = 'https://699340.youcanlearnit.net/image001.jpg'
output_dir = 'images'

download_files(first_url, output_dir)
