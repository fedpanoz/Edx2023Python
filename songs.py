def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

she_loves_you = ["she", "loves", "you", "yeah", "yeah", "yeah",
                    "she", "loves", "you", "yeah", "yeah", "yeah",
                    "she", "loves", "you", "yeah", "yeah", "yeah",
                    "she", "loves", "you", "but", "who", "do", "you",
                    "love", "yeah", "yeah", "yeah"]

beatles = lyrics_to_frequencies(she_loves_you)
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp) 
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

#print(words_often(beatles, 5))
print(type(most_common_words(beatles)))
