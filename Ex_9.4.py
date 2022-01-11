#create a dictionary for sender and find the most popular sender

def main():
    fhand = open('mbox-short.txt')
    counts = dict()
    for line in fhand:
        if line.startswith('From'):
            words = line.split()
            #print(words[1])
            counts[words[1]] = counts.get(words[1],0) + 1
    print(counts)

    sender_most = None
    sender_count = None
    for kkk,vvv in counts.items():
        if sender_most is None or vvv > sender_count:
            sender_most = kkk
            sender_count = vvv
    print(sender_most, sender_count)


if __name__ == '__main__':
    main()