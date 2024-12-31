import http.client
import json
import csv
from time import sleep

headers = {
   'User-Agent': 'insomnia/10.0.0',
   'Content-Type': 'application/json'
}

search_query = """
    query GetSearchTitles(
        $country: Country!
        $language: Language!
        $searchTitlesFilter: TitleFilter
        $searchTitlesSortBy: PopularTitlesSorting! = POPULAR
    ) {
        popularTitles(
            first: 1
            country: $country
            filter: $searchTitlesFilter
            sortBy: $searchTitlesSortBy
        ) {
            edges {
            ...SearchTitleGraphql
            }
        }
    }
    fragment SearchTitleGraphql on PopularTitlesEdge {
        node {
            id
            content(country: $country, language: $language) {
                title
            }
        }
    }
"""

add_to_watchlist_query = """
    mutation SetInWatchlist($input: SetInTitleListInput!) {
        setInWatchlistV2(input: $input) {
            title {
                id
            }
        }
    }

"""

search_variables = {
    "searchTitlesSortBy": "POPULAR",
    "searchTitlesFilter": {
        "objectTypes": [
            ""
        ],
        "excludeIrrelevantTitles": False,
        "includeTitlesWithoutUrl": True,
        "releaseYear": {},
        "searchQuery": ""
    },
    "language": "en",
    "country": "IN"
}

add_to_watchlist_variables = {
	"input": {
		"id": "",
		"state": True
	}
}

def get_id(title, type, year):
    search_filter = search_variables["searchTitlesFilter"]
    search_filter["searchQuery"] = title
    search_filter["releaseYear"] = {
        "min": year
    }
    search_filter["objectTypes"] = type
    search_variables["searchTitlesFilter"] = search_filter
    
    payload = {
        "query": search_query,
        "variables": search_variables
    }

    conn = http.client.HTTPSConnection("apis.justwatch.com")
    try:
        payload_json = json.dumps(payload)
        conn.request("POST", "/graphql", payload_json, headers)
        response = conn.getresponse()
        response_str = response.read().decode()
        json_response = json.loads(response_str)
        return json_response["data"]["popularTitles"]["edges"][0]["node"]["id"]
    except Exception as e:
        print("The title " + title + " could not be found in the justwatch website. So skipping it...")
    finally:
        conn.close()

def add_to_watchlist(id):
    token = '<your_token>'
    headers["Authorization"] = "Bearer " + token
    conn = http.client.HTTPSConnection("apis.justwatch.com")
    try:
        add_to_watchlist_variables["input"]["id"] = id
        payload = {
            "query": add_to_watchlist_query,
            "variables": add_to_watchlist_variables
        }
        payload_json = json.dumps(payload)
        conn.request("POST", "/graphql", payload_json, headers)
        response = conn.getresponse()
        print(response.read().decode())
        return (response.getcode() == 200)
    except Exception as e:
        return
    finally:
        conn.close()
        del headers["Authorization"]

def get_movies_list():
    csv_filename = 'WATCHLIST.csv'
    with open(csv_filename, 'r', encoding = 'ISO-8859-1') as f:
        csv_reader = csv.reader(f, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            title, type, year = row[6], row[8], row[11]
            if(type.endswith("Movie")):
                type = "MOVIE"
            elif(type.endswith("Series")):
                type = "SHOW"
            id = get_id(title, type, year)
            if(id is None):
                continue
            print(title, id)
            
            if(add_to_watchlist(id)):
                print('added ' + title + ' to your watchlist')
            else:
                print("Encountered a problem while adding " + title)
            sleep(1)

if __name__ == '__main__':
    print('Started...')
    get_movies_list()
    print('Imported movies and shows into your justwatch watchlist')
