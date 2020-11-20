import json
import urllib.parse
from app.api.helpers.proxies import proxy_request, session

with open('./app/api/helpers/latlong.json') as latlong:
    lat_long = json.load(latlong)

def create_url(city,page):
    global lat_long
    cord = lat_long[city]
    searchQueryState = {"pagination":{"currentPage":page},"usersSearchTerm":city}
    searchQueryState.update(cord)
    searchQueryState.update({"isMapVisible":False,"filterState":{"sort":{"value":"globalrelevanceex"},"fsba":{"value":False},"fsbo":{"value":False},"nc":{"value":False},"cmsn":{"value":False},"auc":{"value":False},"ah":{"value":True},"pmf":{"value":False}},"isListVisible":True})
    searchQueryState = json.dumps(searchQueryState)
    searchQueryState = urllib.parse.quote(searchQueryState)
    
    url = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={searchQueryState}&wants=".format(searchQueryState=searchQueryState) + r"{%22cat1%22:[%22listResults%22]}&requestId=2"
    return url

def get_address(city):
    url = create_url(city,1)
    response = proxy_request('GET',url)
    try:
        city_data = response.json()
        addresses = set()
        total_pages = int(city_data['cat1']['searchList']['totalPages'])
        cur_res = min(int(city_data['cat1']['searchList']['totalResultCount']), int(city_data['cat1']['searchList']['resultsPerPage']))
        
        for i in range(cur_res):
            addresses.add('"'+city_data['cat1']['searchResults']['listResults'][i]['address']+'"')

        
        for i in range(2,total_pages+1):
            url = create_url(city,i)
            response = proxy_request('GET',url)
            try:
                city_data = response.json()
                cur_res = min(int(city_data['cat1']['searchList']['totalResultCount']), int(city_data['cat1']['searchList']['resultsPerPage']))
            
                for i in range(cur_res):
                    addresses.add('"'+city_data['cat1']['searchResults']['listResults'][i]['address']+'"')
            except:
                continue

        return {'addresses':"\n".join(addresses)}
    except:
        return None