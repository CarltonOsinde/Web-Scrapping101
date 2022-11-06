import time
import requests  #Gets the page source of a website and stores it in a string in python
import selectorlib #Extracts particular information from the page source
import smtplib
import ssl #standard  python libary to send emails via python
import os


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

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "carltonosinde@gmail.com"
    password = "ehlfqfxkhfhmxoia"

    receiver = "carltonosinde@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent!")

def store(extracted):
    with open ("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open ("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        content = read(extracted)

        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey, new event was found")
        time.sleep(2)


