from bs4 import BeautifulSoup as BS         #importing BeautifulSoup for web scraping
import requests                             #importing requests to get raw data of search results page


keyword = input("\nEnter the keyword:\t")   #keyword to search for

img_url = "https://www.google.com/search?q="+keyword+"&source=lnms&tbm=isch"    #search query with keyword

headers={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0"}   #User agent header
site_html = requests.get(img_url, headers).text         #raw html data of the search results page

soup = BS(site_html, "html.parser")         #creating a BeautifulSoup object using the raw data and a html parser


#This code will download the first thumbnail sized photo that it encounters
for element in soup.findAll('img'):
    
    url = element.get("src")            #gets the src link of image
    r = requests.get(url)               #gets the url data

    with open("./img.png", "wb") as photo:      #writes the url data to a file
                photo.write(r.content)
                break
    break                                       #break because 1 picture is enough

#as google doesnt allow webscraping on its search results, we will use an application called google_images_download
#GitHub link to the application: https://github.com/hardikvasa/google-images-download

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()    #creating an object

arguments = {"keywords": keyword, "format": "jpg", "limit":4, "print_urls":True, "size": "medium"}      #function parameters

response.download(arguments)            #downloading the image