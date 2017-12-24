import urllib.request as urllib2
from bs4 import BeautifulSoup
import os

def get_content(url):
    response = urllib2.urlopen(url)
    return response.read()

def links_to_scan(oddanchatram_url):
    html = get_content(oddanchatram_url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("div.article-content h2 a")
    links_to_scan = []
    for link in links:
        href = link['href']
        if not "comments" in href:
            links_to_scan.append(href)
    return links_to_scan

def place_name(file_name):
    places = ["oddanchatram", "dindigul"]
    for place in places:
        if place in file_name:
            return place

def file_path_from_url(url):
    link = url
    links_split_by_slash = link.split('/')
    file_name = links_split_by_slash[3]
    place = place_name(file_name)
    year = file_name.split('-')[-1][-4:]
    directory = "./data/"+place+"/"+year+"/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = directory + file_name +".csv"
    return file_path

def price_scanner(url):
    link = url
    html = get_content(link)
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select("table tr")
    del rows[0]
    array = []
    for row in rows:
        tds = row.select('td')
        if len(tds) == 4:
            sno, name, weight_in_kg, price  = [td.get_text().strip() for td in tds]
            array.append([name, weight_in_kg, price])
        if len(tds) == 3:
            name, weight_in_kg, price  = [td.get_text().strip() for td in tds]
            array.append([name, weight_in_kg, price])
    return array

def url_to_csv(url):
    link = url
    file_path = file_path_from_url(link)
    if not os.path.isfile(file_path):
        array = price_scanner(link)
        rows_to_csv = [', '.join(el) for el in array]
        file_object = open(file_path, "w+")
        file_object.write("Commodity, Weight in Kg, Price in Rs\n")
        for row in rows_to_csv:
            file_object.write(row + "\n")
        file_object.close()
