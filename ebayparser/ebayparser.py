#!python3
import requests
from bs4 import BeautifulSoup as bs
import re

def get_page(url):
    response = requests.get(url)
    print(response.ok)
    print(response.status_code)
    if not response.ok:
        print('Server responded: ', response.status_code)
    else:
        soup = bs(response.text, "lxml")
    return soup

def get_detail_data(soup):
    titles = []
    try:
        title = soup.find_all(['a', 'h3'])
        for element in title:
            if element.find_all(class_="s-item__title"):
                if element.find(class_="s-item__title").get_text()[:11] == 'New Listing':
                    titles.append(element.find(class_="s-item__title").get_text()[11:])
                else:
                    titles.append(element.find(class_="s-item__title").get_text())
    except:
        print("there is a problem with title soup parser")
    titles.pop(0)
    print(len(titles))

    prices = []
    try:
        price = soup.find_all('li')
        for element in price:
            if element.find(class_="s-item__price"):
                prices.append(element.find(class_="s-item__price").get_text())
    except:
        print("there is a problem with price soup parser")
    print(len(prices))

    items_sold = []
    try:
        items = soup.find_all('li')
        for item in items:
            if item.find(class_='BOLD NEGATIVE') and 'sold' in item.find(class_='BOLD NEGATIVE').text:
                m = re.findall('^\d*', item.find(class_='BOLD NEGATIVE').text)
                print(m)
                items_sold.append(m)
            else:
                items_sold.append(None)
            #print(item.find('div').find('span', class_="s-item__hotness s-item__itemHotness").get_text())
    except:
        print("there is a problem with soldnumber soup parser")
    print(len(items_sold))
    #for i in range(len(titles)):
    #    print(titles[i], prices[i])


def main():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=man+watches&_sacat=0'
    get_detail_data(get_page(url))


if __name__ == '__main__':
    main()
