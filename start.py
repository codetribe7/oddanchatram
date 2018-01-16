from lib.lib import *
from lib.date_to_csv import *


for page in range(1, 5):
    page_url = "http://oddanchatramvegetablemarket.com/category/oddanchatram-vegetable-price/page/"+str(page)+"/"
#    page_url = "http://oddanchatramvegetablemarket.com/category/dindigul-vegetable-price/page/"+str(page)+"/"
    links = links_to_scan(page_url)
    for link in links:
        try:
            url_to_csv(link)
        except:
            print(link)

file_name = "dindigul-vegetable-market-price-details-2812017"
places = ["oddanchatram", "dindigul"]
for place in places:
    #print("place:", place)
    if place in file_name:
        print(place)

from lib.lib import *
link = "http://oddanchatramvegetablemarket.com/dindigul-vegetable-market-price-details-112017/"
url_to_csv(link)


# to append the date in files.
dir_path = "./data/"
append_date_column(dir_path)
