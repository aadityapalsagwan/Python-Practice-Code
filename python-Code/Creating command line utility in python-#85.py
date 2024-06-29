# Creating command line utility in python..........


import  argparse
import requests

def DownloadFile(url,local_filename):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return





parser = argparse.ArgumentParser()

# command line argument....
parser.add_argument("url",help = "url of file download")
parser.add_argument("output",help = "by which name do you want to save your file")

# parse  the argument....
args = parser.parse_args()

#use the argument in your code.....
print(args.url)
print(args.output)
DownloadFile(args.url,args.output)