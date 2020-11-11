import requests
import csv
from bs4 import BeautifulSoup


keyword = 'hotels'
location = 'london'
url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1465701626&keywords={}&location={}'.format(keyword, location)
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

datas = []
count_page = 0
for a in range(1, 11):
    count_page+=1
    print('scraping ke :', count_page)
    page = requests.get(url+str(a), headers=headers)
    data = BeautifulSoup(page.text, 'html.parser')
    items = data.findAll('div', 'row businessCapsule--mainRow')
    for i in items:
        nama = i.find('span', 'businessCapsule--name').text
        #sponsored = i.find('span', 'businessCapsule--sponsored').text
        address = ''.join(i.find('span', {'itemprop':'streetAddress'}).text.strip().split('/n'))
        locality = ''.join(i.find('span', {'itemprop':'addressLocality'}).text.strip().split('/n'))
        postalcode = ''.join(i.find('span', {'itemprop':'postalCode'}).text.strip().split('/n'))
        #fungsi .strip().split('/n') menghilangkan spasi(enter), ''.join() menyatukan string
        try : service = i.find('ul','row', {'li':'businessCapsule--serviceBullet'}).text
        except : service = ''
        try : web = i.find('a', {'rel':'nofollow noopener'})['href'].replace('http://','').replace('https://','').split('/')[0]
        except : web = ''
        telp = i.find('span', {'itemprop':'telephone'}).text
        image = i.find('div','col-sm-4 col-md-4 col-lg-5 businessCapsule--leftSide').find('img')['data-original']
        #mencari tag image didalam tag div

        if 'http' not in image: image = 'https://www.yell.com/{}'.format(image)
        #menambahkan string 'https://www.yell.com/' jika website tidak memberikan gambar, fungsi {}.format untuk mengapendkan string tersebut

        datas.append([nama, address, locality, postalcode, web, telp, image])
        print(nama, address,locality,postalcode,web,telp,image)
#header_tabel = ['Name', 'Address', 'City', 'Zip Code', 'Website', 'Phone', 'Image URL']
#writer_csv = csv.writer(open('Hasil/{}_{}.csv'.format(keyword, location), 'w', encoding='utf-8', newline=''))
#writer_csv.writerow(header_tabel)
#for b in datas: writer_csv.writerow(b)