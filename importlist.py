import requests
import urllib.parse
import json
import csv
from time import sleep

headers = {
    'authority': 'apis.justwatch.com',
    'accept': 'application/json, text/plain, */*',
    'origin': 'https://www.justwatch.com',
    'referer': 'https://www.justwatch.com/in/watchlist',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
}

def get_movies_list():
    csv_filename = 'WATCHLIST.csv'
    movies_list = list()
    with open(csv_filename, 'r', encoding = 'ISO-8859-1') as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                line_count += 1
                movie_with_year = row[5] + ' ' + row[10]
                movies_list.append(movie_with_year)
            else:
                line_count += 1
    return movies_list

def add_to_watchlist(obj_id, obj_type):
    justwatch_id = ''
    authorization = ''
    url = ('https://apis.justwatch.com/personalization/title_list/watchlist/object_type/{0}/object_id/{1}?justwatch_id={2}').format(obj_type, obj_id, justwatch_id)
    if 'authorization' not in headers:
        headers['authorization'] = authorization
    requests.put(url, headers=headers)

if __name__ == '__main__':
    print('importing in progress...')
    url = 'https://apis.justwatch.com/content/titles/en_IN/popular?body='
    query_param = {
        'page_size': 1,
        'content_types': [
            'show',
            'movie'
        ]
    }
    movies_list = get_movies_list()
    for movie in movies_list:
        query_param['query'] = movie
        request_url = url + urllib.parse.quote(json.dumps(query_param))
        try:
            response = requests.get(request_url, headers=headers)
            json_response = response.json()
            object_id = json_response["items"][0]["id"]
            object_type = json_response["items"][0]["object_type"]
            add_to_watchlist(object_id, object_type)
        except Exception as e:
            print("The title " + movie + " could not be found in the justwatch website. So skipping it...")
            continue
        print('added ' + movie + ' to your watchlist')
        sleep(3)
    print('finished importing movies and shows to your justwatch watchlist')