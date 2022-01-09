#find specific text in a txt file

def main():
    fname = input('Enter file name to open:')
    fhand = open(fname)
    count = 0
    dspam_confidence = 0

    for line in fhand:
        if line.__contains__('X-DSPAM-Confidence: '):
            num_str = line[20:].rstrip()
            print(num_str)
            x = float(num_str)
            dspam_confidence += x 
            count += 1

    print('total confidence:', dspam_confidence)
    print('line count', count)
    print('average confidence is ', dspam_confidence/count)


if __name__ == '__main__':
    main()