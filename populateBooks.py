#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import csv
import urllib.request
import requests

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.WARNING)

def DownloadBookList():
    url = "https://gist.githubusercontent.com/jaidevd/23aef12e9bf56c618c41/raw/c05e98672b8d52fa0cb94aad80f75eb78342e5d4/books.csv"
    urllib.request.urlretrieve(url, "books.csv")


def RegisterExists(url, user, password, model, field, register):
    logging.debug(f'REGISTER EXIST FUNCTION in model {model}')
    url = url + model + '/?' + field + '=' + register
    logging.debug(f'\turl: {url}')
    r = requests.get(url, auth=(user, password))
    logging.debug(f'\tstatus_code: {r.status_code}')
    if r.status_code == 200:
        if len(r.json()) == 1:
            rDict = r.json()[0]
            logging.debug(f'\tregister exists with id: {rDict["id"]}')
            return rDict['id']
        else:
            logging.debug(f'\tregister doesnt exists')
            return 0


def AddRegister(url, user, password, model, data):
    logging.debug(f'ADD REGISTER FUNCTION in model {model}')
    url = url + model + '/'
    logging.debug(f'\turl: {url}')
    r = requests.post(url, data=data, auth=(user, password))
    logging.debug(f'\tstatus_code: {r.status_code}')
    if r.status_code == 201:
        rDict = r.json()
        logging.debug(f'\tregister added with id: {rDict["id"]}')
        return rDict['id']
    else:
        logging.error('caca' + r.text)


def PopulateBooks(url, user, password):
    with open('books.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                title = row[0]
                author = row[1]
                genre = row[2]
                if author == '':
                    author = 'Unknown'

                bookReg = RegisterExists(url, user, password, "book", "title", title)
                if bookReg == 0:
                    logging.debug(f'title: {title} doesn\'t exists')
                    genreReg = RegisterExists(url, user, password, "genre", "name", genre)

                    if genreReg == 0:
                        logging.debug(f'\tgenre: {genre} doesn\'t exists')
                        genreData = {'name': genre}
                        genreReg = AddRegister(url, user, password, "genre", genreData)

                    stockData = {'quantity': '5'}
                    quantityReg = AddRegister(url, user, password, "stock", stockData)

                    genreLink = url + 'genre/' + str(genreReg) + '/'
                    quantityLink = url + 'stock/' + str(quantityReg) + '/'

                    bookData = {'title': title, 'author': author, 'genre': genreLink, 'quantity': quantityLink,
                            'price': '15.50', 'register_date': '1982-12-17'}
                    print("\n\tdata: " + str(bookData))
                    bookReg = AddRegister(url, user, password, 'book', bookData)

            line_count += 1
        logging.debug(f'Processed {line_count} books.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate Bookstore")
    parser.add_argument("-v", "--verbose", help="Show info of the process", action="count", default=0)
    parser.add_argument("-u", "--user", type=str, help="User of the Bookstore API rest", default='admin')
    parser.add_argument("-p", "--password", type=str, help="Password of the Bookstore API rest", default='admin')
    parser.add_argument("-a", "--address", type=str, help="URL of the Bookstore API rest", default='http://127.0.0.1:8000/')

    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(logging.INFO)
    else:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        DownloadBookList()
    except:
        logging.error("Error trying to download data")
    else:
        logging.debug("Books.csv file downloaded")

    PopulateBooks(args.address, args.user, args.password)
