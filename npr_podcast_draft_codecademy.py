from urllib2 import urlopen
from urllib2 import quote
npr_id = raw_input("Enter comma-seperated NPR IDs or leave blank.")
search_string = raw_input("Enter your search string or leave blank.")
feed_title = raw_input("What's your feed title?")
key = "API_KEY"
url = 'http://api.npr.org/query?apiKey='
url += key
url += "&numResults=3"
url += "&action=Or"
url += "&requiredAssets=audio"
url += "&format=Podcast"

if npr_id or search_string == True:
    raw_input("Hit Enter to download your podcast")
    if npr_id:
        url += "&id=" + npr_id
    if search_string:
        url += "&searchTerm=" + str(quote(search_string))
    if feed_title:
        url += "&title=" + str(quote(feed_title))
else:
    print "You must enter an NPR ID, a search term, or both."