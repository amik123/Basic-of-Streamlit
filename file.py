def word_count(filepath):
    word_frequency=dict()
    with open(filepath,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('./,:"?')
                word_frequency[word]=word_frequency.get(word,0)+1
    return word_frequency


print(word_count('sample.txt'))
