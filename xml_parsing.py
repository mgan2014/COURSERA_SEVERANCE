import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

def main():
    url_input = input('Enter url:')
    fhand = urllib.request.urlopen(url_input)
    data = fhand.read()
    print(data)
    
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print('count:', len(counts))
    total = 0
    for each_count in counts:
        total += int(each_count.text)
    print('total:', total)
    

if __name__ == '__main__':
    main()