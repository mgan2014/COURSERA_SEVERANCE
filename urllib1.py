import urllib.request, urllib.parse, urllib.error

def main():

    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand: 
        words = line.decode().split() 
        print(words)


if __name__ == '__main__':
    main()

