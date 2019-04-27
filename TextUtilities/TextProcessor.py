from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from textblob import TextBlob
import random
import re
import json

"""
str = r'Hello might be derived from hullo, which the American Merriam-Webster dictionary describes as a "chiefly British variant of hello," and which was originally used as an exclamation to call attention, an expression of surprise, or a greeting.The word hullo is still in use, with the meaning hello.The use of hello as a telephone greeting has been credited to Thomas Edison; according to one source, he expressed his surprise with a misheard Hullo.Bill Bryson asserts in his book Mother Tongue that "hello" comes from Old English hál béo þu (see also "goodbye" which is a contraction of "God be with you".According to the Oxford English Dictionary, hello is an alteration of hallo, hollo, which came from Old High German "halâ, holâ, emphatic imperative of halôn, holôn to fetch, used especially in hailing a ferryman."'
str = json.dumps(str)
regex = re.compile("\((.*?)\)")
str = re.sub( regex, ' ', str)
regex = re.compile("\[(.*?)\]")
str = re.sub( regex, ' ', str)
str = re.sub(r'\s+', ' ', str)
print(sent_tokenize(str))
"""

def getProcessedTextualData(text):
    return TextBlob(text)

def replaceIC(word, sentence):
    insensitive_hippo = re.compile(r"\b"+word+r"\b", re.IGNORECASE)
    return insensitive_hippo.sub('__________________', sentence)

def getSentences(line):
    regex = re.compile("\((.*?)\)")
    line = re.sub( regex, ' ', line)
    regex = re.compile("\[(.*?)\]")
    line = re.sub( regex, ' ', line)
    #regex = line.strip('\"\'')
    regex = re.compile("\"")
    line = re.sub(regex, ' ', line)
    line = re.sub(r'\s+', ' ', line)
    
    return sent_tokenize(line)

    

def getWordEmbedding(fileName):
    word_embeddings = {}
    f = open( fileName, encoding='utf-8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32') 
        word_embeddings[word] = coefs
    f.close()
    return word_embeddings

def removePunctuation(sentences):
    clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")
    clean_sentences = [s.lower() for s in clean_sentences]
    return clean_sentences


def removeStopwords(sentenceList):
    stop_words = stopwords.words('english')
    newSentences = []
    for sentence in sentenceList:
        sentenceNew = " ".join([i for i in sentence.split() if i not in stop_words])
        newSentences.append(sentenceNew)
    return newSentences

def removeWordFromSentence(sentence, poss):
    words = None
    words = poss.get(b'NN')
    words = None
    temp1 = None
    temp1 = poss.get(b'NNP')
    temp2 = poss.get(b'NN')
    poss2 = {}
    count=0
    for key, value in poss.items(): 
        x = key.decode("utf-8")
        temp = []
        for iter in value:
            y = iter.decode("utf-8")
            temp.append(y)
        poss2[x] = temp
        count+=1
    if 'NNP' in poss2:
        words = poss2['NNP']
    elif 'NN' in poss2:
        words = poss2['NN']
    else:
        print("NN and NNP not found")
        return (None, sentence, None)
    if len(words) > 0:
        word = random.choice(words)
        replaced = replaceIC(word, sentence)
        return (word, sentence, replaced)
    else:
        print("words are empty")
        return (None, sentence, None)





    

    

    