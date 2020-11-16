#import modules
import requests
import numpy as np


#create headers if requests.get not found 404
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://shopee.co.id/search'
}
#url = 'https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword=baju%20anak&limit=50&newest='+str(page)+'&order=desc&page_type=search&version=2'
count=0
pages = np.arange(1, 101, 50)#total 100 data
for p in pages:
    url = 'https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword=baju%20anak&limit=50&newest=' + str(p) + '&order=desc&page_type=search&version=2'
    r = requests.get(url+str(p), headers=header).json()
    prod = r['items']
    for i in prod:
        prod_name = i['name']
        sold = i['historical_sold']
        brand = i['brand']
        price = round(i['price'] / 100000)
        rating = round(i['item_rating']['rating_star'])
        shop_id = i['shopid']
        view = i['view_count']
        item_id = i['itemid']
        url_1 = 'https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}'.format(item_id, shop_id)
        a = requests.get(url_1).json()
        stock = a['item']['normal_stock']
        kat = a['item']['categories'][0]['display_name']
        sub_kat = a['item']['categories'][1]['display_name']
        sub_sub_kat = a['item']['categories'][2]['display_name']
        url_2 = 'https://shopee.co.id/api/v2/shop/get?is_brief=1&shopid={}'.format(shop_id)
        b = requests.get(url_2).json()
        shop_name = b['data']['name']
        count += 1
        print(count, ':', shop_name, prod_name, sold, view, price, rating, stock, kat, sub_kat, sub_sub_kat, shop_id)

