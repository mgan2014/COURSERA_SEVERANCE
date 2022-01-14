#find 'hour'

def main():
    fhand = open('mbox-short.txt')
    hours_list = dict()
    for line in fhand:
        if line.startswith('From'):
            strings = line.split()
            #print(strings)
            if len(strings) > 5:
                email_time = strings[5]
                #print(email_time)
                email_hour = email_time.split(':')[0]
                #print(email_hour)
                hours_list[email_hour] = hours_list.get(email_hour, 0) + 1
    print(sorted(hours_list.items()))

if __name__ == '__main__':
    main()