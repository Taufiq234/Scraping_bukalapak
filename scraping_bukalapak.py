import requests
import csv
from bs4 import BeautifulSoup


file_name = 'scraping iphone 10 bukalapak'
write = csv.writer(open('hasil/{}.csv'.format(file_name), 'w', newline=''))
header_field = ['No', 'Shop Name', 'Product Name', 'Price', 'Condition', 'Stock', 'Sold', 'Rating Average', 'City', 'Image']
write.writerow(header_field)

url = 'https://api.bukalapak.com/multistrategy-products'
count =0
count_page=0
for page in range(1, 16): #15 pages
    count_page+=1
    parameter = {
        'prambanan_override' : True,
        'category_name' : 'HP & Smartphone',
        'category_id' : 8,
        'keywords' : 'iphone 10',
        'limit' : 100,
        'offset' : 0,
        'page' : 1,
        'facet' : True,
        'access_token' : 'XLkqezqvY0mfQ4uczEoMCBQSHVaAefhR9mhxwOcaXlb6Xw' # don't forget to update access_token
    }

    data = requests.get(url, params=parameter).json()
    products = data['data']
    for i in products:
        shop_name = i['store']['name']
        name_prod = i['name']
        price_prod = i['price']
        condition_prod = i['condition']
        stock_prod = i['stock']
        sold_prod = i['stats']['sold_count']
        rat_prod = i['rating']['average_rate']
        city = i['store']['address']['city']
        img  = i['images']['large_urls']
        count += 1
        write = csv.writer(open('hasil/{}.csv'.format(file_name), 'a', newline=''))
        data = [count, shop_name, name_prod, price_prod, condition_prod, stock_prod, sold_prod, rat_prod, city, img]
        write.writerow(data)


    #print('Name :', name_prod, 'Price :', price_prod, 'Condition :', condition_prod, 'Stock :',stock_prod, 'Sold :', sold_prod, 'Rating :', rat_prod, 'Shop Name :', shop_name, 'City :', city, 'Image :', img)
