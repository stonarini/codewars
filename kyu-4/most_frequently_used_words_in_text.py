# https://www.codewars.com/kata/51e056fe544cf36c410000fb
# Most Frequently Used Words in Text

# First Implementation 18/10/2021
import re
def top_3_words(text):
    words=[word.lower() for word in text.split()]
    filter=re.compile('.*[^a-zA-Z\']+.*')
    filter_qmark=re.compile("[\']+")
    for i in range(len(words)):
        if filter.match(words[i]):
            filtered_word=""
            for letter in words[i]: 
                if not filter.match(letter):
                    filtered_word+=letter
                else:
                    words.append(filtered_word)
                    filtered_word=""
            words[i]=filtered_word
            
    word_count={word:words.count(word) for word in words if word != '' or filter_qmark.match(word)} 
    top_word_count=[]
    for i in range(len(word_count)):
        highest_count=max(word_count, key= lambda x: word_count[x])
        if filter_qmark.match(highest_count):
            word_count.pop(highest_count)
            continue
        top_word_count.append(highest_count)
        word_count.pop(highest_count)
        if len(top_word_count) == 3: break
        
    return(top_word_count)