#parse JSON data string

import urllib.request, urllib.parse, urllib.error
import json

def main():
    #get url data
    url = input('Enter url:')
    fh = urllib.request.urlopen(url)
    data = fh.read()

    #parse json
    all_data = json.loads(data)
    comments = all_data["comments"]
    print('count:', len(comments))
    total = 0
    for comment in comments:
        total += int(comment['count'])
    print('total:', total)

if __name__ == '__main__':
    main()