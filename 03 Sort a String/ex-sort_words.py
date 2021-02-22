def sort_words(words):
    # step 1: get the word list
    words_list = words.split(' ')
    
    # step 2: sort the words alphabetically
    words_lower = []
    for i, j in enumerate(words_list):
        words_lower.append(j.lower()+str(i))
    
    words_lower.sort()
    
    # step 3: join the words
    new = ["".join(words_list[int(i[-1])]) for i in words_lower]
    return new

if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))