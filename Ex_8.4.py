#find unique words

def main():
    fname = input('Enter file name:')
    fhand = open(fname)
    whole_file = fhand.read()
    word_list = whole_file.split()
    unique_list = list()
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    print('total words in ', fname, ':', len(whole_file))
    print('number of unique words:', len(unique_list))
    print(unique_list)

if __name__ == '__main__':
    main()