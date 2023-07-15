import time
import random
import json

import requests
from bs4 import BeautifulSoup

maxCrawledPages = 300


def sleep():
    sleepTime = 3 + random.randrange(0, 3)
    print(f'SLEEP: {sleepTime}')
    time.sleep(sleepTime)


def crawler(seed, domain):
    frontier = [seed]
    crawled = set()
    headers = {
        "User-Agent": "Student bot"
    }
    file = open('./results/products.json', 'w')
    file.write('[')
    crawledPages = 0
    fileIsEmpty = True
    while frontier and crawledPages <= maxCrawledPages:
        page = frontier.pop(0)
        try:
            print('CRAWLED: ' + page)
            resp = requests.get(page, headers=headers)
            print(f'STATUS CODE:  {resp.status_code}')
            crawledPages += 1

            if resp.status_code != 200 and resp.status_code != 201:
                crawled.add(page)
                sleep()
                print()
                continue

            source = resp.text
            soup = BeautifulSoup(source, "html5lib")
            products = [heading.a for heading in soup.findAll('h5')]
            recommendedProducts = [heading.a for heading in soup.findAll('h3')]

            try:
                productDetail = soup.select_one('div#product-detail')
                priceAction = productDetail.select_one(
                    'div.pd-price-wrapper').select_one('span.price')
                product = {}

                # name
                product['name'] = productDetail.h1.text.strip()

                # price with out vat
                product['price without vat'] = priceAction.select_one(
                    'span.price-vatex').text.replace("\xa0", " ").strip()

                # price with vat
                product['price with vat'] = priceAction.select_one(
                    'span.price-vatin').text.replace("\xa0", " ").strip()

                # stock info
                product['stock info'] = ' '.join(productDetail.select_one(
                    'span.availability-state-on-stock').text.replace("\xa0", " ").strip().split(" ")[:3])

                # url
                product['url'] = page

                # description
                description = productDetail.select_one(
                    'p.pd-shortdesc').text.replace("\xa0", " ").strip()
                newLineIdx = description.find('\n')
                product['description'] = description[:newLineIdx]

                file.write("\n" if fileIsEmpty else ",\n")
                file.write(json.dumps(product))
                fileIsEmpty = False
            except Exception as e:
                print(e)
                sleep()

            print()
            if page not in crawled:
                for link in products:
                    if domain + link['href'] not in crawled:
                        frontier.append(domain + link['href'])
                for link in recommendedProducts:
                    if domain + link['href'] not in crawled:
                        frontier.append(domain + link['href'])
                crawled.add(page)
            sleep()

        except Exception as e:
            crawled.add(page)
            print(e)
            sleep()

    file.write('\n]')
    file.close


print(crawler('https://www.czc.cz/iphone-mobilni-telefony/produkty', 'https://www.czc.cz'))
