# find senders' names in the email file

def main():
    fname = input('Enter file name:')
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith('From'):
            sender = line.split()[1]
            print(sender)
            count +=1
    print('There are %d emails' % count)

if __name__ == '__main__':
    main()