
# First import wget python module.
import wget
import shutil
from datetime import datetime
import os

dt = datetime.now()
data = dt.strftime("%d-%m-%Y %H-%M-%S")
image = 'Snapshot'+data+'.jpeg'
# cmd = f"wget http://169.254.142.233:8080/?action=snapshot -o output"+data+".jpg"
os.system(f"wget http://169.254.142.233:8080/?action=snapshot -o output.jpeg")
#image_url = "http://admin:19319@169.254.142.233:8080/?action=snapshot"

# Downloading image
#local_image_filename = wget.download(image_url, image)

#basedir = os.path.abspath(os.path.dirname('__path__'))
#dest = os.path.join(basedir, 'static\\images')

#shutil.move(image, dest)

"""
image_url = 'https://image.shutterstock.com/image-photo/colorful-flower-on-dark-tropical-260nw-721703848.jpg'
# Invoke wget download method to download specified url image.
local_image_filename = wget.download(image_url, 'output.jpg')

# shutil.move(local_image_filename, '/static/images')

# Print out local image file name.
print(local_image_filename)
"""
"""

import urllib.request
import random


def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)
    print(full_file_name)


downloader('http://admin:19319@169.254.142.233:8080/?action=snapshot')
"""
