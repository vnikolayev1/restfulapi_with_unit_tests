def mul(number, times):
    return(float("%.2f" % (number**times)))

def group_words(words):
    sorted_words = []
    grouped_words = {}
    cnt = 0
    #  transfering words to dict where keys are letters 2,3,4
    for word in words:
        #  add word if key exists
        if len(word) < 4:
            #  adding "special symbol" for prevention of mixing keys
            grouped_words["free" + str(cnt)] = [word]
            cnt += 1
        elif word[1:4] in grouped_words:
            grouped_words[word[1:4]].append(word)
        else:
            #  add key and value otherwise
            grouped_words[word[1:4]] = [word]
    #  transfering grouped values to the list
    for val in grouped_words.items():
        sorted_words.append(val[1])
    sorted_words.sort(key=lambda x:x[0] , reverse=True)
    sorted_words.sort(key=len, reverse=True)
    return(sorted_words)

def seri(text):
    #  splitting string over -> combination, deleting whitespaces
    parsed_text = [words.strip() for words in text.split('->')]
    parsed_text = ["{'" + word + "':" for word in parsed_text]
    parsed_text.append("''" + "}" * len(parsed_text))
    #  transforming list into string
    result = ''.join(parsed_text)
    return(result)