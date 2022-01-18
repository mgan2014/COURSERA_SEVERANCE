#find all the numbers in a txt file and calculate the average
import re

def main():
    fhand = open('mbox-short.txt')
    total = 0
    count = 0
    for line in fhand:
        n = re.findall('[0-9]+\.*[0-9]+', line)
        if (len(n)) > 0:
            #print(n)
            for x in n:
                print(x)
                total += float(x)
                count += 1
    print(int(total/count))

        

if __name__ == '__main__':
    main()