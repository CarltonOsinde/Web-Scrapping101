import requests  #Gets the page source of a website and stores it in a string in python
import selectorlib #Extracts particular information from the page source


URL = "https://programmer100.pythonanywhere.com/tours/"

#Scraping the page source from the URL
def scrape(url):
    response = requests.get(url)
    source =  response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value




if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)


