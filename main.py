from bs4 import BeautifulSoup as BS
import requests


keyword = input("\nEnter the keyword:\t")

img_url = "https://www.google.com/search?q="+keyword+"&source=lnms&tbm=isch"

headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}
site_html = requests.get(img_url, headers).text

soup = BS(site_html, "html.parser")


f = open("site.txt", "w")
f.write(site_html)

#This code will download the first thumbnail sized photo that it encounters
for element in soup.findAll('img'):
    url = element.get("src")
    print(url)
    r = requests.get(url)
    with open("./img.png", "wb") as photo:
                photo.write(r.content)
                break
    break

#as google doesnt allow webscraping on its search results, we will use an application called google_images_download
#GitHub link to the application: https://github.com/hardikvasa/google-images-download

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload() 

arguments = {"keywords": keyword, "format": "jpg", "limit":4, "print_urls":True, "size": "medium"}

response.download(arguments)