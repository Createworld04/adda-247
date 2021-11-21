import requests
import subprocess

link = input ("Enter Link :- ")
hs = requests.get(link).headers
cookie = hs["Set-Cookie"].replace(", ",";")
link = link.split("&param=")[0]
newlink = link.replace("e-books?file=","")
name = newlink.replace("https://store.adda247.com/","").replace(".doc",".pdf").replace("http://store.adda247.com/","")
print(f'Downloading :- "{name}"')
dl = subprocess.run(f'aria2c "{newlink}" --header "cookie: {cookie}" -o "{name}"', shell=True)
if dl.returncode == 0:
    print("\nDownload successfull....")
else:
    print("\nDownload Failed....")