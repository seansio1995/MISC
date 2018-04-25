import requests
import os
import shutil

global dump

def download_file(url):
    global dump
    url = url
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file(url):
    filename=url.split("/")[-1]
    global dump
    location = os.path.abspath("/Users/tfsp-h/Desktop/TensorflowSlides/"+filename)
    with open(filename, 'wb') as location:
        shutil.copyfileobj(dump, location)
    del dump

os.mkdir("/Users/tfsp-h/Desktop/TensorflowSlides")

for i in range(14):
    try:
        if i+1 < 10:
            url="http://web.stanford.edu/class/cs20si/lectures/slides_0{}.pdf".format(i+1)
            download_file(url)
            save_file(url)
        else:
            url="http://web.stanford.edu/class/cs20si/lectures/slides_{}.pdf".format(i+1)
            download_file(url)
            save_file(url)
    except:
        print("Error downloading the file")
