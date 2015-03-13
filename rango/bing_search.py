import json
import urllib, urllib2

from sys import argv

# Add your BING_API_KEY

BING_API_KEY = '3mikAzGOgW2NcARUynT/xyqaNy+2mUuDe1+TZRILUJs'

def run_query(search_terms):
    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'

    results_per_page = 10
    offset = 0

    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    username = ''

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, search_url, username, BING_API_KEY)
# Create our results list which we'll populate.
    results = []
    try:
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(search_url).read()
        json_response = json.loads(response)

        for result in json_response['d']['results']:
            results.append({
                'title': result['Title'],
                'link': result['Url'],
                'summary': result['Description']})
# Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError, e:
        print "Error when querying the Bing API: ", e
# Return the list of results to the calling function.
    return results

def main(argv):
    search_input = argv[1][:10]
    search_results = run_query(search_input)
    counter=0
    while counter<10:
        search_item = search_results[counter]
        print counter+1, " Title =", search_item['title'], " Url =", search_item['link']," Description =", search_item['summary']
        counter+=1

if __name__ == '__main__':
    main(argv)
