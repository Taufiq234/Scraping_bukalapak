#import modules
import requests
import csv



file_name = 'scraping baju anak shopee'
write = csv.writer(open('hasil/{}.csv'.format(file_name), 'w', newline=''))
header_field = ['No', 'Product Name', 'Sold', 'Brand', 'Price', 'Rating', 'Stock', 'Categories',
                'Sub Categories', 'Sub Sub Categories', 'Shop ID']
write.writerow(header_field)

#create headers if requests.get not found 404
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://shopee.co.id/search'
}
url = 'https://shopee.co.id/api/v2/search_items'
count=0
for page in range(1,16):
    parameter = {
        'by': 'relevancy',
        'keyword': 'baju anak',
        'limit': 50,
        'newest': 0,
        'order': 'desc',
        'page_type': 'search',
        'version': 2
    }
    r = requests.get(url, headers=header, params=parameter).json()
    # print(data.status_code)
    prod = r['items']
    for i in prod:
        prod_name = i['name']
        sold = i['historical_sold']
        brand = i['brand']
        price = round(i['price']/100000)
        rating = round(i['item_rating']['rating_star'])
        shop_id = i['shopid']
        item_id = i['itemid']
        url_1 = 'https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}'.format(item_id, shop_id)
        parameter_1 = {
            'limit': 50,
        }
        a = requests.get(url_1, params=parameter).json()
        stock = a['item']['normal_stock']
        kat = a['item']['categories'][0]['display_name']
        sub_kat = a['item']['categories'][1]['display_name']
        sub_sub_kat = a['item']['categories'][2]['display_name']
        count += 1
        write = csv.writer(open('hasil/{}.csv'.format(file_name), 'a', encoding='utf-8', newline=''))
        isi = [count,prod_name,sold,brand,price,rating,stock,kat,sub_kat,sub_sub_kat,shop_id]
        write.writerow(isi)

#        print(count,':',prod_name,sold,price,price_max,rating,stock,kat,sub_kat,sub_sub_kat,shop_id)
