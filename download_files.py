import sys
import os
from urllib.request import urlopen
from urllib.parse import unquote
from urllib.error import URLError

def download_file(download_url):
    save_file = os.path.basename(unquote(download_url))
    try:
        response = urlopen(download_url)
        with open(save_file, 'wb') as pdf:
            pdf.write(response.read())
        print("File '" + save_file + "' has been downloaded.")
    except URLError as e:
        if e.code == 404:
            print("404 error on URL: " + download_url)
        else:
            print("{error} on URL: '{url}'".format(error=e, url=download_url))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit('Must provide at least 1 URL')
    else:
        for index, url in enumerate(sys.argv):
            if index == 0:
                # first index is the name of the script
                continue
            else:
                download_file(url)
      print('Finished!')
